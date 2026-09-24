import { useState } from "react";
import "./App.css";
const API = import.meta.env.VITE_API_URL;
function App() {
  const [task, setTask] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
const runAgent = async () => {
  if (!task.trim()) return;

  setLoading(true);
  setResult("");

  try {
    const response = await fetch(
      "https://evomind-ouhh.onrender.com/agent/execute",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ task }),
      }
    );

    if (!response.ok) {
      throw new Error(`Backend error: ${response.status}`);
    }

    const data = await response.json();

    setResult(
      data.result?.result ||
      data.result ||
      JSON.stringify(data, null, 2)
    );
  } catch (error) {
    console.error(error);

    setResult(
      "Could not connect to EvoMind backend."
    );
  }

  setLoading(false);
};
 

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="logo">
          <div className="logo-icon">E</div>
          <div>
            <h2>EvoMind</h2>
            <span>AI Platform</span>
          </div>
        </div>

        <nav>
          <div className="nav-item active">⚡ AI Agent</div>
          <div className="nav-item">🔄 Workflows</div>
          <div className="nav-item">🧠 Memory</div>
          <div className="nav-item">🔧 Tools</div>
          <div className="nav-item">🧬 Evolution</div>
        </nav>

        <div className="sidebar-bottom">
          <span className="online-dot"></span>
          System Online
        </div>
      </aside>

      <main className="main">
        <header>
          <div>
            <p className="eyebrow">AUTONOMOUS AI SYSTEM</p>
            <h1>AI Command Center</h1>
            <p className="subtitle">
              Orchestrate agents, tools, workflows and adaptive intelligence.
            </p>
          </div>

          <div className="status">
            <span className="online-dot"></span>
            Backend Connected
          </div>
        </header>

        <section className="stats">
          <div className="card">
            <span>AGENTS</span>
            <strong>4</strong>
            <small>Orchestrator + sub-agents</small>
          </div>

          <div className="card">
            <span>TOOLS</span>
            <strong>1</strong>
            <small>Universal tool layer</small>
          </div>

          <div className="card">
            <span>WORKFLOWS</span>
            <strong>1+</strong>
            <small>Reusable automation</small>
          </div>

          <div className="card">
            <span>MEMORY</span>
            <strong>ON</strong>
            <small>Behavioral preferences</small>
          </div>
        </section>

        <section className="command-panel">
          <div className="panel-header">
            <div>
              <h2>Command Agent</h2>
              <p>Give EvoMind a task and let the orchestrator decide what to do.</p>
            </div>
            <span className="badge">ORCHESTRATOR</span>
          </div>

          <textarea
            value={task}
            onChange={(e) => setTask(e.target.value)}
            placeholder="Try: Calculate 125 * 8"
          />

          <button onClick={runAgent} disabled={loading}>
            {loading ? "Running..." : "▶ Run Agent"}
          </button>

          {result && (
            <div className="result">
              <div className="result-title">Agent Result</div>
              <pre>{result}</pre>
            </div>
          )}
        </section>

        <section className="architecture">
          <h2>System Architecture</h2>

          <div className="architecture-grid">
            <div>
              <b>USER</b>
              <span>Task / Intent</span>
            </div>

            <div className="arrow">→</div>

            <div>
              <b>ORCHESTRATOR</b>
              <span>Task Routing</span>
            </div>

            <div className="arrow">→</div>

            <div>
              <b>SUB-AGENTS</b>
              <span>Research · Writer · Automation</span>
            </div>

            <div className="arrow">→</div>

            <div>
              <b>TOOLS + RAG</b>
              <span>Capabilities & Knowledge</span>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
