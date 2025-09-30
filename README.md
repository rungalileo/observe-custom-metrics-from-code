# Galileo Custom Metrics Demo

This demo shows how to fetch and display custom metrics from the Galileo API after running LLM calls.

## Files

- **`logstreams/logstream_demo.py`** - Runs LLM calls with Galileo logging
- **`logstreams/fetch_session_metrics.py`** - Fetches and displays session metrics
- **`logstreams/fetch_logstream_metrics.py`** - Fetches and displays logstream metrics
- **`experiments/create_dataset.py`** - Creates a dataset for legal advice detection testing
- **`experiments/run_experiment.py`** - Runs an experiment using the dataset to test metrics
- **`experiments/fetch_experiment.py`** - Fetches and displays experiment results by ID
- **`env.template`** - Environment variables template
- **`README.md`** - This file

## Setup

1. Install dependencies:
```bash
pip install galileo openai python-dotenv requests
```

2. Set up environment variables:
```bash
# Copy the template and fill in your values
cp env.template .env
# Edit .env with your actual credentials
```

Required environment variables:
- `GALILEO_API_KEY` - Your Galileo API key
- `GALILEO_PROJECT` - Your Galileo project name
- `GALILEO_PROJECT_ID` - Your Galileo project ID
- `GALILEO_LOG_STREAM` - Your Galileo log stream
- `GALILEO_CONSOLE_URL` - Your Galileo console URL
- `GALILEO_API_URL` - Your Galileo API URL
- `OPENAI_API_KEY` - Your OpenAI API key

## Usage

### Step 1: Run LLM calls
```bash
python logstreams/logstream_demo.py
```

### Step 2: Fetch metrics (in another terminal or after waiting)
```bash
# Fetch session metrics
python logstreams/fetch_session_metrics.py <session_id>

# Fetch logstream metrics (all sessions in a logstream)
python logstreams/fetch_logstream_metrics.py
# OR with explicit project and logstream names
python logstreams/fetch_logstream_metrics.py "My Project" "My Logstream"
```

### Step 3: Create dataset for testing (optional)
```bash
python experiments/create_dataset.py
```

### Step 4: Run experiment (optional)
```bash
python experiments/run_experiment.py
```

### Step 5: Fetch experiment results (optional)
```bash
python experiments/fetch_experiment.py <experiment_id>
```

## What it does

### `logstreams/logstream_demo.py`:
1. **Runs legal advice LLM calls** with Galileo logging
2. **Shows contrast** between legal and non-legal questions
3. **Displays session ID** for metrics fetching

### `logstreams/fetch_session_metrics.py`:
1. **Fetches session metrics** from Galileo API
2. **Displays comprehensive metrics** from all levels (session, trace, span)
3. **Shows custom metrics** like legal advice detection

### `logstreams/fetch_logstream_metrics.py`:
1. **Fetches all metrics for a logstream** using environment variables or explicit arguments
2. **Uses sessions, traces, and spans search** with pagination to get complete data
3. **Returns hierarchical JSON** with all sessions, traces, and spans in the logstream
4. **Environment variables**: `GALILEO_PROJECT` and `GALILEO_LOG_STREAM`
5. **Command-line usage**: `python fetch_logstream_metrics.py "Project Name" "Logstream Name"`

### `experiments/create_dataset.py`:
1. **Creates a dataset** with legal advice input-output pairs
2. **Contains examples** where users ask for legal advice
3. **Shows proper refusals** where the system politely declines to give legal advice
4. **Perfect for testing** the "Legal Advice Offered" metric

### `experiments/run_experiment.py`:
1. **Fetches the dataset** by name
2. **Runs an experiment** using the dataset
3. **Tests the "Legal Advice Offered" metric** on all dataset examples
4. **Uses a simple LLM function** similar to the demo
5. **Provides experiment ID** for fetching results separately

### `experiments/fetch_experiment.py`:
1. **Fetches experiment results** by ID from Galileo API
2. **Displays comprehensive results** including metrics and feedback
3. **Shows dataset information** and experiment details
4. **Standalone script** for fetching any experiment results

## Output

The demo will show:
- LLM responses
- Polling progress
- Session metrics
- Trace metrics  
- Span metrics
- Metric info with status and values
