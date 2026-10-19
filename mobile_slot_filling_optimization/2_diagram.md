# Diagram: Optimizing On-Device Slot Filling on a Phone

## 1. Request pipeline (what runs on each turn)

```mermaid
flowchart LR
  A[User speech or text] --> B[Rule normalize<br/>dates, numbers]
  B --> C[Short prompt<br/>fixed prefix first]
  C --> D{Prefix in<br/>KV cache?}
  D -- yes --> E[Process new tokens only]
  D -- no --> F[Process full prompt]
  E --> G[llama-server<br/>Q4 model, json_schema,<br/>n_predict = 64]
  F --> G
  G --> H[Parse and validate]
  H --> I[Merge state]
```

## 2. Where the time goes

```
Total latency
├── Load model          (avoid: start server once)
├── Read prompt         (reduce: short prompt + cache_prompt)
│   └── Prefill tokens
└── Write output        (reduce: n_predict = 64, JSON stops early)
    └── Decode tokens
```

## 3. Optimization levers

```mermaid
flowchart TD
  M[Goal: fast, accurate, low memory] --> L1[Smaller model<br/>0.5B-1.5B, Q4_K_M]
  M --> L2[Shorter prompt<br/>fixed prefix + cache_prompt]
  M --> L3[Limited output<br/>n_predict, temperature 0]
  M --> L4[Small context<br/>-c 512 to 1024]
  M --> L5[Warm server<br/>start once, -np 1]
  M --> L6[Hardware tuning<br/>threads, GPU/NPU layers]
  M --> L7[Rules first<br/>dates and numbers in code]
  L1 --> V{Accuracy test<br/>still passes?}
  L2 --> V
  L3 --> V
  L4 --> V
  L5 --> V
  L6 --> V
  L7 --> V
  V -- no --> U[Undo last change]
  V -- yes --> K[Keep change, measure again]
```

## 4. Lever table

| Lever | Change | Effect | Risk |
|---|---|---|---|
| Model size | 1.5B → 0.5B, Q4_K_M | Less memory, faster decode | Lower accuracy |
| Prompt cache | `cache_prompt: true`, fixed prefix first | Less prefill per turn | Prefix must not change |
| Output limit | `n_predict: 64` | Stops long output | Truncated JSON if too small |
| Context | `-c 1024` instead of 4096 | Less memory per step | Long dialogs need state trimming |
| Warm server | Start `llama-server` once | Removes load time | Background memory use |
| Threads | Match fast cores (test 2 / 4 / 6) | Faster inference | Heat and battery |
| Rules | Normalize dates and numbers in code | Fewer model errors | More code to maintain |

## 5. Measurement loop

```
 Baseline ──► change ONE lever ──► measure latency + memory
    ▲                                      │
    │                                      ▼
  undo ◄──── accuracy drop? ◄──── accuracy test on same set
                                           │ no drop
                                           ▼
                                    keep, next lever
```
