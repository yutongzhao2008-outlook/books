# How to Optimize On-Device Slot Filling on a Phone

Topic: optimize `slot_filling_ondevice.html` on a phone.
Rules: short sentences. One idea per sentence. Simple words.

## Why it is slow

1. The model runs on the phone.
2. The phone has less memory than a server.
3. The phone has less compute than a server.
4. Speed depends on three costs.
5. The first cost is reading tokens. The prompt is read every turn.
6. The second cost is writing tokens. The model writes one token at a time.
7. The third cost is loading the model. Loading takes seconds.

## What to do

### 1. Make the model smaller

8. Use a model of 0.5 billion or 1.5 billion parameters.
9. Use Q4_K_M quantization.
10. A smaller model uses less memory.
11. A smaller model runs faster.
12. Accuracy can fall. Test it.

### 2. Keep the prompt short

13. Put the fixed text first.
14. Keep the fixed text the same on every turn.
15. Turn on `cache_prompt`.
16. The cached part is not read again.
17. Send only the new user words after the fixed part.

### 3. Limit the output

18. Set `n_predict` to 64.
19. The output is one small JSON object.
20. Stop when the JSON closes.
21. Set `temperature` to 0.

### 4. Keep the context small

22. Use `-c 512` to `-c 1024`.
23. A long context uses more memory.
24. A long context also slows each step.

### 5. Start the server once

25. Start `llama-server` once when the app starts.
26. Keep it running.
27. Do not load the model on each request.

### 6. Use the phone's hardware

28. Set the thread count to the number of fast CPU cores.
29. Test 2, 4, and 6 threads.
30. Use GPU or NPU layers only if your build supports them.
31. Test each change on a real device.

### 7. Use rules before the model

32. Convert dates in code. "明天" becomes `2026-10-20`.
33. Convert numbers in code.
34. Do not let the model do date math.
35. The model only extracts. Code decides.

### 8. Measure before and after each change

36. Measure first-token latency.
37. Measure total latency.
38. Measure peak memory.
39. Measure again after five minutes. Phones slow down when hot.
40. Change one thing at a time.

### 9. Check accuracy after each change

41. Run the same test set after each change.
42. Speed does not matter if the slots are wrong.
43. If accuracy drops, undo the last change.

## Summary

44. Make the model smaller.
45. Keep the prompt short and cached.
46. Limit the output.
47. Keep the server running.
48. Let code handle dates and numbers.
49. Measure, then change one thing.
