
# AI Debug Agent

A project that uses a custom AI agent (powered by Gemini ) to automatically detect, fix, and test bugs in Python code. 
The agent can inspect code files, write patches, run tests, and verify results — all via function tools.

---

##  Repository Structure

├── calculator/ # Contains the calculator module / logic
├── functions/ # Definitions of tool functions (get file content, write file, run code, etc.)
├── call_function.py # Dispatches function calls from the AI agent to the tool functions
├── config.py # Configuration (if any)
├── main.py # Agent entry point, orchestrates prompting, tool calls, and responses
├── tests.py # Test suite (expressions + behaviors) used to validate fixes
├── pyproject.toml # Project metadata & dependencies
├── .gitignore

---



##  What it Does

This agent does the following:

- Reads existing project files (code & tests)  
- Understands bug reports/prompt from user  
- Writes fixes to source code (for example: correct operator precedence in calculator)  
- Runs tests to confirm the fix works  
- Reports back what it changed  

Essentially automates debugging & patching workflows in a controlled way.

---

##  How to Set Up & Run

1. **Clone the repo**  
   
   git clone https://github.com/aqeel-01/ai-debug-agent.git
   cd ai-debug-agent

2. **Set up virtual environment**

python -m venv .venv
# Activate it:
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# or Command Prompt:
.venv\Scripts\activate.bat
# On Linux / Mac:
source .venv/bin/activate


3. **Install dependencies**
If you use pyproject.toml, probably via poetry or pip:

pip install -r requirements.txt
# or if using poetry:
poetry install


4. **Configure API key**
Make sure to set your Gemini / genai API key via environment variable, e.g.:

export GEMINI_API_KEY="your_api_key_here"
# or on Windows:
set GEMINI_API_KEY="your_api_key_here"


5. **Run the agent**
Use a prompt telling the agent what bug to fix. For example:

uv run main.py "fix the bug: 3 + 7 * 2 should not be 20" --verbose

Or run the calculator directly:

uv run calculator/main.py "3 + 7 * 2"


Run tests manually (if needed):

python tests.py

## Example

Before fix:
Expression 3 + 7 * 2 incorrectly evaluates to 20.

After running the agent:
The agent patches the calculator module to respect operator precedence.
Tests pass. Expression shows correct result (17).

## How It Works Internally

main.py: handles user prompts, calls Gemini via genai, passes messages for context, handles tool calls & responses.

functions/: tools that Gemini uses: reading files, writing files, running Python code, etc.

call_function.py: dispatcher that takes a function_call object and invokes the right tool.

calculator module: actual code that has bugs to be fixed.

tests.py: provides test cases so the agent can validate its fixes.

## Known Limitations & Future Work

Currently work is session-based: agent memory does not persist across restarts.

Tests are limited; more edge cases could be added.

Could integrate auto-PR or CI bots to accept fixes automatically.

Expand to support more file types, languages, and refactoring scenarios.

