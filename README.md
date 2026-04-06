# tiffany-personal-algorithms
This is a repo with some algorithms that I needed to debug. Since I don't have LeetCode or NeetCode premium, I need to run locally for my debugger. Most debugging is done in VS Code and test cases are in main (I thought of using a separate test suite, but then I couldn't debug from there).

Honestly I'm also not sure which ones are finished or not finished. TBD on some write-ups.

## Linked List Problems
LinkedListProblems.py has various methods for LinkedList problems. 

## Testing LLMs
Specifically for testing some LLMs. The criteria is less than 3GB RAM, which usually meant around 1-3 billion parameters. My context window is set to 4000 MB, which is small, but for algorithm problems like this, I shouldn't need a large context window.

Each model will be tested on the following questions:
- Write a Bubble Sort in Python
- Write a Max-Heap class using Python without external libraries.
- Write an iterative Merge Sort in Python
  - Modified: Write a top-down iterative Merge Sort in Python

Then graded on accuracy without reprompting (one-shot).

### llama3.2:3b

[Model details](https://ollama.com/library/llama3.2:3b):
- architecture: llama
- parameters: 3.21B
- quantization: Q4_K_M

Size is about 2.0 GB for 3 billion parameters. Meta's text-based LLM. Able to follow instructions, summarize, rewrite prompts, and use tools. [Ollama link](https://ollama.com/library/llama3.2)

- Bubble Sort: flawless
- Max-Heap: like Heapq, good
  - Cons: Swaps are not Pythonic; uses a temp variable like in pseudocode or other programming languages
- Iterative Merge Sort: failed, wrote recursive
  - Pros: Iterative top-down merge sort almost worked - just had to adjust one variable value
  - Cons: Needed reprompting with better language to write recursive Merge Sort

llama3.2 writes standard algorithms well and even some advanced ones like a top-down merge sort. Function comments follow standard practice (showing inputs/outputs at the start of functions) and in-depth explanations are provided at the end.

### smollm2:1.7b

[Model details](https://ollama.com/library/smollm2:1.7b):
- architecture: llama
- parameters: 1.71B
- quantization: Q8_0

Size is about 1.8 GB for 1.7 billion parameters. I think SmolLM is made by HuggingFace? Or HuggingFace is a platform for a community.

- Bubble Sort: flawless
  - Pros: writes fast, because minimal notes there's no fluff
  - Cons: No provided tests, minimal notes for educational purposes
- Max Heap: flawless
  - Pros: writes fast, writes Pythonic and cleanly
  - Cons: minimal notes, no explanation (possibly could prompt for it)
- Merge Sort: recursive fine, iterative not
  - Pros: Recursive works well, is Pythonic and compact
  - Cons: Iterative does not work (only sorts pairs, not the whole list), had to reprompt for recursive (will test with others that pass initial prompt)

  Overall I think this is the best small LM for working, worst for education. It makes minimal mistakes.

## phi4-mini:3.8b

[Model details](https://ollama.com/library/phi4-mini:3.8b):
- architecture: phi3
- parameters: 3.84B
- quantization: Q4_K_M

Size is about 2.5 GB for 3.8 billion parameters. The phi series is Microsoft's open source LLM series. 

- Bubble Sort: works
  - Pros: written well, includes early quit condition, has notes
- Max Heap: 
- Iterative Merge Sort: not working
  - Pros: phi4-mini:3.8b is aware that its implementation of iterative merge sort is not working
  - Cons: phi4-mini:3.8b still gave a bad merge sort

## dolphin-phi:2.7b

[Model details](https://ollama.com/library/dolphin-phi:2.7b):
- architecture: phi2
- parameters: 2.78B
- quantization: Q4_0

## deepseek-r1:1.5b

[Model details](https://ollama.com/library/llama3.2:3b):
- architecture: qwen2
- parameters: 1.78B
- quantization: Q4_K_M

## gemma3:1b

[Model details](https://ollama.com/library/gemma3:1b):
- architecture: gemma3
- parameters: 1000M
- quantization: Q4_K_M

Size is about 800 MB for 1 billion parameters. Gemma is built on Google's Gemini. Supposedly excels in tasks like question answering, summarization, and reasoning

- Bubble Sort: good
  - Pros: Comments show expected input/output, lots of educational explanation
- Max Heap: not working
  - Pros: Cleanly-written code
  - Cons: comments about expected outputs are off, heapify_down doesn't work (looks at parent index instead of child index), tried prompting again for heapify_down and was still incorrect
- Merge Sort: not working, not close
  - Pros: prompting for normal recursive MergeSort works
  - Cons: Iterative merge sort doesn't work at all, recursive merge sort isn't written in a Pythonic way

I had high hopes for gemma3, however the 1b version is too small to work pretty much. Tried gemma3:270m just out of curiosity and it's too dumb to know what Merge Sort is. I think gemma3:1b is too dumb to use.

### himanshu231204/hk-devbrain:v3 

[Model details](https://ollama.com/himanshu231204/hk-devbrain:v3):
- architecture: llama
- parameters: 3.21B
- quantization: Q4_K_M

Size is 2 GB for 3 billion parameters. Modified version of llama3.2 for coding purposes (3rd party).
- Bubble Sort: flawless
- Max-Heap: like heapq, good
    - extract_max method iterates through the whole heap for max when max is root
    - swap is more Pythonic
- Iterative Merge Sort: Fail, doesn't work
    - Does try to do it iteratively but in doing so, it does it wrong
    - Merge Sort goes from left to right instead of merging in a divide-and-conquer manner
Compared to llama3.2, which is the base version, hk-debrain is wordier, but I don't think that's to its benefit. Both fail at iterative Merge Sort, which was just a test to see if they can do weird algorithms. However hk-devbrain:v3 failed to write a working sort.

## qwen2.5-coder:3b

[Model details](https://ollama.com/library/qwen2.5-coder:3b):
- architecture: qwen2
- parameters: 3.09B
- quantization: Q4_K_M

Size is about 986 MB for 3 billion parameters. Qwen is I believe an Alibaba subsidiary. They offer a range of models from general purpose to coding-specific. The qwen2.5:3b model is the best in terms of parameters-to-size ratio, but does more parameters translate to better performance?

- Bubble Sort: good
  - Pros: Detailed algorithm explanation; fast
  - Cons: No comments or type hinting for expected input/output type
- Max Heap: fail
  - Note: Indexing starts at 1, which is more human
  - Cons: No separate heapify, heap_up, or heap_down function (all embedded in insert and delete), no __str__ function to print 1-indexed heap, so prints using sliced [1:] each time, is_leaf method is incorrect (I think because uses wrong length)
- Merge Sort: fail
  - Cons: didn't do an iterative implementation, recursive implementation is wrong (got confused)

I am severely unimpressed with qwen2.5-coder:3b. The accuracy is much lower than for llama3.2:3b even though the number of parameters is the same. I will not use in the future.


## qwen3.5:0.8b

[Model details](https://ollama.com/library/qwen3.5:0.8b):
- architecture: qwen35
- parameters: 873M
- quantization: Q8_0

Size is about 1.0 GB for 1 billion parameters. The qwen3.5 model is a more recent version than qwen2.5, so I am hopeful that its accuracy is also better.


- Bubble Sort: flawless
  - Pros: lots of in-line comments
  - Cons: No comments or type-hinting for input/output types, time analysis is BS (0, 2.56, and 3.0 are not big-O things)
- Max Heap: completely wrong
  - Cons: Conflating heap with node class, index out of range error in set_max_value because never adds value to heap
- Merge Sort: not it fam
  - Pros: Merge sort works
  - Cons: notes are nonsensical, text repeats itself, not iterative

Truly, this one is very stupid, unusable in my opinion.

## other ones tried (not formal)

### codegemma:2b

[Model details](https://ollama.com/library/codegemma:2b):
- architecture: gemma
- parameters: 2.51B
- quantization: Q4_0

Just noting for myself that I tried this one and it's too dumb. I tried to ask it for a bubble sort and it spat out nonsense and blank lines before giving me an algorithm. It did give me bubble sort and merge sort, which both work, but it's annoying to get when there's better lightweight options.

### deepseek-coder:1.3b

[Model details](https://ollama.com/library/deepseek-coder:1.3b):
- architecture: llama
- parameters: 1.35B
- quantization: Q4_0

- super light, 700 MB for 1.3 billion parameters
- asked for binary search and it repeated a line again and again for some reason
- dumbest one so far unfortunately
- do not use

### samuser3/granite3.2-gemma3:1b

[Model details](https://ollama.com/samuser3/granite3.2-gemma3:1b):
- architecture: qwen3
- parameters: 752M
- quantization: Q4_K_M

Note: 1B is the lightweight version, text support only

- Least RAM usage, about 1 GB
- Not smart at all, can only trust it with very simple algorithms
- Doesn't run with Claude Code
- removing just because not smart