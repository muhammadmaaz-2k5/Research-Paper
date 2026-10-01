import base64
import os
import subprocess

def main():
    img_path = r'c:\Users\RYZEN 7\Desktop\Thesis\RsearchPaper\assets\graph_rag_text_to_sql.jpg'
    img_b64 = ""
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            img_b64 = base64.b64encode(f.read()).decode('utf-8')

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Research Proposal - Muhammad Maaz Khan</title>
<style>
    @page {{
        size: A4;
        margin: 13mm 15mm 13mm 15mm;
    }}
    body {{
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
        color: #1f2937;
        line-height: 1.4;
        font-size: 9pt;
        background: #ffffff;
        margin: 0;
        padding: 0;
    }}
    .header {{
        border-bottom: 2px solid #1e3a8a;
        padding-bottom: 8px;
        margin-bottom: 10px;
    }}
    .badge {{
        display: inline-block;
        background: #e0e7ff;
        color: #1e40af;
        padding: 2px 7px;
        font-size: 7.5pt;
        font-weight: 700;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 3px;
    }}
    h1 {{
        font-size: 13.5pt;
        color: #1e3a8a;
        margin: 2px 0 5px 0;
        line-height: 1.25;
        font-weight: 700;
    }}
    .meta-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 6px;
        font-size: 8.5pt;
        background: #f8fafc;
        padding: 7px 10px;
        border-radius: 5px;
        border: 1px solid #e2e8f0;
    }}
    .meta-item strong {{
        color: #0f172a;
    }}
    .abstract-box {{
        background: #f0fdf4;
        border-left: 3.5px solid #16a34a;
        padding: 7px 10px;
        margin: 8px 0 10px 0;
        font-size: 8.5pt;
        border-radius: 0 5px 5px 0;
    }}
    .abstract-title {{
        font-weight: 700;
        color: #15803d;
        text-transform: uppercase;
        font-size: 7.5pt;
        letter-spacing: 0.5px;
        margin-bottom: 2px;
    }}
    h2 {{
        font-size: 10.5pt;
        color: #0f172a;
        border-bottom: 1px solid #cbd5e1;
        padding-bottom: 2px;
        margin-top: 8px;
        margin-bottom: 4px;
        font-weight: 700;
    }}
    p {{
        margin: 0 0 5px 0;
        text-align: justify;
    }}
    .diagram-container {{
        text-align: center;
        margin: 6px 0 8px 0;
        page-break-inside: avoid;
    }}
    .diagram-container img {{
        max-width: 95%;
        max-height: 195px;
        height: auto;
        border-radius: 5px;
        border: 1px solid #cbd5e1;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    .diagram-caption {{
        font-size: 7.5pt;
        color: #64748b;
        margin-top: 2px;
        font-style: italic;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 7.5pt;
        margin: 6px 0;
        page-break-inside: avoid;
    }}
    th, td {{
        border: 1px solid #cbd5e1;
        padding: 4px 6px;
        text-align: left;
    }}
    th {{
        background: #f1f5f9;
        font-weight: 600;
        color: #0f172a;
    }}
    tr:nth-child(even) {{
        background: #f8fafc;
    }}
    .timeline-table td {{
        padding: 3px 5px;
    }}
    .footer {{
        border-top: 1px solid #e2e8f0;
        padding-top: 4px;
        margin-top: 8px;
        font-size: 7pt;
        color: #64748b;
        display: flex;
        justify-content: space-between;
    }}
    .page-break {{
        page-break-before: always;
    }}
    ul, ol {{
        margin: 0 0 5px 0;
        padding-left: 16px;
    }}
    li {{
        margin-bottom: 1.5px;
    }}
</style>
</head>
<body>

<!-- PAGE 1 -->
<div class="header">
    <div class="badge">Graduate Research Proposal &bull; USTC 2026/2027 Admissions</div>
    <h1>Relational Graph-Aware Schema Retrieval for Robust Text-to-SQL over Complex Enterprise Databases</h1>
    <div class="meta-grid">
        <div class="meta-item">
            <strong>Applicant:</strong> Muhammad Maaz Khan<br>
            <strong>Undergraduate Degree:</strong> BS Computer Science, UET Peshawar<br>
            <strong>Target Degree:</strong> Master of Science (MS) in Computer Science
        </div>
        <div class="meta-item">
            <strong>Prospective Supervisor:</strong> Prof. Shuangwu Chen (Associate Professor)<br>
            <strong>Host Institution:</strong> School of Computer Science & Technology, USTC<br>
            <strong>Target Funding:</strong> CAS-ANSO Scholarship for Young Talents
        </div>
    </div>
</div>

<div class="abstract-box">
    <div class="abstract-title">Executive Abstract</div>
    Natural Language Interfaces to Databases (NLIDB) translate conversational user questions into executable SQL queries. Building upon recent breakthroughs in table reasoning such as <strong>SQLForge (ACL 2025)</strong>, <strong>Table Pruning in TableQA (ACL 2026 Oral)</strong>, and <strong>SpecCache for RAG Serving (ACL 2026 Oral)</strong> from Prof. Shuangwu Chen's laboratory, enterprise databases with dozens to hundreds of interconnected tables pose severe schema-linking and foreign-key join bottlenecks. Conventional Retrieval-Augmented Generation (RAG) models schemas as independent text blocks, retrieving tables through semantic vector similarity. Over multi-table relational structures, vector retrieval frequently retrieves terminal tables while omitting essential intermediate junction tables, triggering invalid joins, column hallucinations, and execution failures. This proposal presents <strong>Relational Graph-RAG</strong>, a framework that models database metadata as a directed relational knowledge graph. By executing structural path traversals across foreign-key dependencies, the system isolates the minimal connected subgraph required to bridge user entities, supplying LLMs with structurally sound, hallucination-resistant context. Evaluated against direct prompting and vector-RAG baselines on public benchmarks (Spider, BIRD), this research investigates the trade-offs between execution accuracy, token efficiency, and schema scalability.
</div>

<h2>1. Introduction & The Core Problem</h2>
<p>
Modern enterprise databases (ERP, CRM, and financial data lakes) enforce relational integrity through normalized schemas comprising dozens to hundreds of tables linked by primary and foreign keys. When a user asks an analytical question such as <em>"What were total electronics sales purchased by Computer Science students in 2025?"</em>, answering requires constructing a multi-table SQL query joining five distinct entities: <code>departments &rarr; users &rarr; orders &rarr; products &rarr; categories</code>.
</p>
<p>
Standard Large Language Models encounter severe degradation on such queries. If the entire database schema is provided in the prompt, context windows quickly saturate, incurring prohibitive token costs and triggering <em>"Lost-in-the-Middle"</em> attention decay. Conversely, if naive semantic vector retrieval is employed, the retriever selects tables that match query keywords (e.g., <code>departments</code> and <code>products</code>) but omits the bridging junction tables (<code>users</code> and <code>orders</code>). Consequently, the LLM hallucinates non-existent foreign keys or produces syntactically broken queries.
</p>

<h2>2. Relational Graph-RAG System Architecture</h2>
<p>
Extending the table reasoning and pruning foundations established in <strong>SQLForge (ACL 2025)</strong> and <strong>Table Pruning in TableQA (ACL 2026 Oral)</strong>, <strong>Relational Graph-RAG</strong> formalizes the database as a directed relational knowledge graph G = (V, E). Vertices V represent tables and attribute columns; directed edges E represent primary-foreign key relationships, constraints, and cardinalities.
</p>

<div class="diagram-container">
    <img src="data:image/jpeg;base64,{img_b64}" alt="Relational Graph-RAG for Text-to-SQL Architecture">
    <div class="diagram-caption">Figure 1: End-to-end Relational Graph-RAG architecture showing automated schema graph compilation, multi-hop path search, Redis subgraph caching, and closed-loop SQL AST verification.</div>
</div>

<p>
The system executes a four-stage query lifecycle:
</p>
<ol>
    <li><strong>Automated Schema Mining:</strong> An automated ingestion daemon queries PostgreSQL/MySQL metadata (<code>information_schema.tables</code>, <code>columns</code>, <code>key_column_usage</code>) to dynamically construct the relational graph without manual tagging.</li>
    <li><strong>Multi-Hop Path Traversal:</strong> An entity extractor maps natural language query concepts to graph nodes. A shortest-path graph search (evaluating Dijkstra and Steiner tree algorithms) identifies the minimal connected join subgraph connecting all target entities.</li>
    <li><strong>Sub-Millisecond Redis & Speculative Caching:</strong> Frequently accessed schema paths (e.g., <code>orders &rarr; payments &rarr; users</code>) are cached in Redis to eliminate redundant graph traversal latencies, interfacing seamlessly with speculative KV-cache reuse techniques (SpecCache).</li>
    <li><strong>Closed-Loop SQL AST Validation:</strong> Candidate SQL emitted by the LLM is parsed using an Abstract Syntax Tree (AST) validator (<code>sqlglot</code>) before database execution. If an invalid column or unconstrained join is detected, structured diagnostic feedback is fed back to the model for zero-shot self-correction.</li>
</ol>

<div class="footer">
    <span>Candidate: Muhammad Maaz Khan (muhammadmaaz.dev@gmail.com)</span>
    <span>Host Institution: School of Computer Science & Technology, USTC</span>
    <span>Page 1 of 3</span>
</div>

<!-- PAGE 2 -->
<div class="page-break"></div>

<h2>3. Controlled 3-Stage Experimental Methodology</h2>
<p>
To establish empirical academic rigor, the framework will be benchmarked through a controlled comparative evaluation across three distinct systems on standardized public datasets (Spider cross-domain benchmark and BIRD enterprise database benchmark):
</p>

<table>
    <thead>
        <tr>
            <th>Experimental Stage</th>
            <th>Context Generation Mechanism</th>
            <th>Input Token Footprint</th>
            <th>Hypothesized Failure Mode</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Stage 1: Direct Prompting</strong></td>
            <td>Full raw schema dump (DDL) passed in prompt</td>
            <td>~35,000 – 50,000 tokens</td>
            <td>High token cost, context window saturation, attention decay</td>
        </tr>
        <tr>
            <td><strong>Stage 2: Standard Vector RAG</strong></td>
            <td>Dense vector embeddings (top-k semantic similarity)</td>
            <td>~6,000 – 8,000 tokens</td>
            <td>Omits intermediate junction tables; broken multi-table joins</td>
        </tr>
        <tr>
            <td><strong>Stage 3: Relational Graph-RAG</strong></td>
            <td>Minimal connected subgraph with explicit join constraints</td>
            <td>~2,500 – 4,000 tokens</td>
            <td><strong>Hypothesis:</strong> Eliminates hallucinations, achieves highest execution accuracy</td>
        </tr>
    </tbody>
</table>

<h2>4. Quantitative Evaluation Metrics</h2>
<p>
The evaluation will measure six precise quantitative metrics:
</p>
<ul>
    <li><strong>Execution Accuracy (EX %):</strong> Percentage of generated queries that execute and return exact ground-truth tabular results.</li>
    <li><strong>Schema-Linking Recall (SL %):</strong> Proportion of ground-truth tables, columns, and foreign keys correctly identified.</li>
    <li><strong>Valid SQL Compilation Rate (VSR %):</strong> Proportion of generated queries that parse and compile with zero syntax errors.</li>
    <li><strong>Token Consumption Efficiency:</strong> Total prompt token overhead compared against baseline schema prompting.</li>
    <li><strong>End-to-End Query Latency (P50/P99):</strong> Processing time encompassing retrieval, generation, AST validation, and execution.</li>
    <li><strong>Schema Scale Robustness:</strong> Degradation profile as database schema scales from 10 &rarr; 50 &rarr; 200 tables.</li>
</ul>

<h2>5. 24-Month Master's Research & Academic Roadmap</h2>
<table class="timeline-table">
    <thead>
        <tr>
            <th style="width: 24%;">Academic Phase</th>
            <th style="width: 48%;">Core Research Activities</th>
            <th style="width: 28%;">Milestones & Deliverables</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Year 1: M1 – M3</strong></td>
            <td>Core graduate coursework; systematic literature review on schema linking; scientific Python & PyTorch training.</td>
            <td>Course completion; formal literature review document.</td>
        </tr>
        <tr>
            <td><strong>Year 1: M4 – M6</strong></td>
            <td>Build automated PostgreSQL/MySQL metadata extractor; configure Spider/BIRD benchmark testbeds.</td>
            <td>Reproducible Baseline A & B implementation.</td>
        </tr>
        <tr>
            <td><strong>Year 1: M7 – M9</strong></td>
            <td>Implement NetworkX schema graph compiler and multi-hop Steiner tree search heuristics.</td>
            <td>Working Relational Graph-RAG prototype.</td>
        </tr>
        <tr>
            <td><strong>Year 1: M10 – M12</strong></td>
            <td>Execute preliminary comparative benchmarks; analyze schema-linking recall and latency profiles.</td>
            <td>Annual laboratory review presentation; refined methodology.</td>
        </tr>
        <tr>
            <td><strong>Year 2: M13 – M15</strong></td>
            <td>Integrate SQL AST self-correction loop; test hybrid retrieval (dense embedding + graph search).</td>
            <td>Closed-loop verification pipeline verified.</td>
        </tr>
        <tr>
            <td><strong>Year 2: M16 – M18</strong></td>
            <td>Conduct full ablation studies (varying schema size, graph search vs vector search); error taxonomy.</td>
            <td>Complete experimental result corpus & graphs.</td>
        </tr>
        <tr>
            <td><strong>Year 2: M19 – M21</strong></td>
            <td>Compile thesis chapters (Introduction, Related Work, Architecture, Experiments, Discussion).</td>
            <td>Full Master's thesis draft; conference submission if warranted.</td>
        </tr>
        <tr>
            <td><strong>Year 2: M22 – M24</strong></td>
            <td>Thesis revision based on committee review; final defense; experimental codebase archiving.</td>
            <td><strong>Master's Thesis Defense & Degree Completion.</strong></td>
        </tr>
    </tbody>
</table>

<div class="footer">
    <span>Candidate: Muhammad Maaz Khan (muhammadmaaz.dev@gmail.com)</span>
    <span>Host Institution: School of Computer Science & Technology, USTC</span>
    <span>Page 2 of 3</span>
</div>

<!-- PAGE 3 -->
<div class="page-break"></div>

<h2>6. Candidate Background, Feasibility, & Supervision Fit</h2>
<p>
<strong>Preparation & Practical Systems Readiness:</strong> I hold a Bachelor of Science in Computer Science from the University of Engineering and Technology (UET), Peshawar, Pakistan. Over the past 4+ years, I have worked professionally as a backend and full-stack software engineer architecting production databases (PostgreSQL, MySQL), distributed caching layers (Redis), and containerized microservices (Docker). While I do not possess prior academic publications, my daily experience designing relational schemas, writing complex multi-table joins, and debugging database bottlenecks provides immediate practical readiness to construct database extractors and experimental testbeds from Day 1. I am committed to dedicating Year 1 coursework to mastering theoretical machine learning and empirical research methodologies.
</p>
<p>
<strong>Direct Alignment with Prof. Shuangwu Chen's Group:</strong> Prof. Shuangwu Chen's laboratory at USTC is a recognized leader in table intelligence and efficient RAG serving, evidenced by recent groundbreaking publications including <em>SQLForge</em> (ACL 2025 Findings), <em>Table Pruning in TableQA</em> (ACL 2026 Oral), <em>Dual Denoising for Large-Scale Tables</em> (ACL 2026), and <em>SpecCache for RAG Serving</em> (ACL 2026 Oral). My proposed research on graph-guided multi-table join discovery extends his team's table pruning and reasoning paradigms from flat tables into deeply normalized relational enterprise schemas. Under Prof. Chen's supervision, I aim to combine applied database systems engineering with rigorous table reasoning research.
</p>

<h2>7. Key Research Questions & Anticipated Contributions</h2>
<p>
The thesis will formally answer three primary research questions:
</p>
<ul>
    <li><strong>RQ1:</strong> Does relational-graph-aware schema retrieval significantly improve Execution Accuracy (EX) over multi-table queries compared to standard vector retrieval baselines on Spider and BIRD benchmarks?</li>
    <li><strong>RQ2:</strong> By what factor does subgraph context pruning reduce token consumption and generation latency across varying schema sizes?</li>
    <li><strong>RQ3:</strong> How effectively does an AST-guided verification loop detect and self-repair relational join errors prior to database execution?</li>
</ul>
<p>
<strong>Expected Contributions:</strong> (1) An open-source, reproducible Relational Graph-RAG schema extraction and retrieval pipeline; (2) A comprehensive benchmark evaluation across varying enterprise schema complexities (10 to 200 tables); and (3) An empirically validated Master's thesis advancing natural language database interfaces.
</p>

<h2>8. Selected Foundational References</h2>
<ul style="font-size: 7.5pt; color: #475569; line-height: 1.35;">
    <li>[1] Guo, Y., Chen, S.*, et al. "SQLForge: Synthesizing Reliable and Diverse Data to Enhance Text-to-SQL Reasoning in LLMs." <em>Findings of ACL 2025</em>.</li>
    <li>[2] Guo, Y., Ye, S., Chen, S., Yang, J. "Rethinking Table Pruning in TableQA: From Sequential Revisions to Gold Trajectory-Supervised Parallel Search." <em>ACL 2026 (Oral)</em>.</li>
    <li>[3] Ye, S., Guo, Y., Chen, S., Yang, J. "When TableQA Meets Noise: A Dual Denoising Framework for Complex Questions and Large-scale Tables." <em>ACL 2026</em>.</li>
    <li>[4] Wen, Z., Zhang, T., Chen, S., Yang, J. "SpecCache: Speculative KV Cache Reuse for Efficient RAG Serving." <em>ACL 2026 (Oral)</em>.</li>
    <li>[5] Li, J., et al. "Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQL (BIRD)." <em>NeurIPS 2023</em>.</li>
</ul>

<div class="footer">
    <span>Candidate: Muhammad Maaz Khan (muhammadmaaz.dev@gmail.com)</span>
    <span>Host Institution: School of Computer Science & Technology, USTC</span>
    <span>Page 3 of 3</span>
</div>

</body>
</html>
"""

    html_file = r'c:\Users\RYZEN 7\Desktop\Thesis\RsearchPaper\proposal_template.html'
    pdf_file = r'c:\Users\RYZEN 7\Desktop\Thesis\RsearchPaper\Muhammad_Maaz_Khan_Research_Proposal_Graph_RAG_USTC.pdf'

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    cmd = [
        edge_exe,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--run-all-compositor-stages-before-draw',
        f'--print-to-pdf={pdf_file}',
        html_file
    ]

    print("Running Edge headless print-to-pdf for Prof. Shuangwu Chen...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_file):
        size = os.path.getsize(pdf_file)
        print(f"SUCCESS: Clean 3-Page Academic PDF generated for Prof. Shuangwu Chen at {pdf_file} ({size} bytes)")
    else:
        print("ERROR: PDF was not generated. Return code:", res.returncode)

if __name__ == '__main__':
    main()
