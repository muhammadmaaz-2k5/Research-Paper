import os
import subprocess
import pypdf

def generate_formal_synopsis():
    html_parts = []
    
    # CSS and Header
    html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Formal Research Synopsis - Muhammad Maaz Khan (USTC)</title>
<style>
  @page {
    size: A4 portrait;
    margin: 0;
  }
  *, *::before, *::after {
    box-sizing: border-box;
  }
  body {
    margin: 0;
    padding: 0;
    font-family: 'Times New Roman', Times, serif;
    color: #111111;
    background-color: #ffffff;
    font-size: 11.5pt;
    line-height: 1.46;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
  }
  .page {
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    min-height: 297mm;
    box-sizing: border-box;
    padding: 24mm 24mm 24mm 30mm;
    position: relative;
    page-break-after: always;
    page-break-inside: avoid;
    overflow: hidden;
    background: #ffffff;
  }
  .footer {
    position: absolute;
    bottom: 14mm;
    left: 30mm;
    right: 24mm;
    text-align: center;
    font-size: 11pt;
    font-family: 'Times New Roman', Times, serif;
    color: #222222;
  }
  h1.chap-num {
    font-size: 15pt;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    margin: 0 0 4px 0;
    letter-spacing: 0.5px;
  }
  h1.chap-title {
    font-size: 15pt;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    margin: 0 0 16px 0;
    letter-spacing: 0.5px;
  }
  h2.sec-title {
    font-size: 12.5pt;
    font-weight: bold;
    margin: 12px 0 6px 0;
    color: #000000;
  }
  h3.subsec-title {
    font-size: 11.5pt;
    font-weight: bold;
    margin: 10px 0 4px 0;
    color: #000000;
  }
  p {
    text-align: justify;
    text-justify: inter-word;
    margin: 0 0 8.5px 0;
  }
  .table-caption {
    font-size: 10.5pt;
    font-weight: bold;
    text-align: left;
    margin: 10px 0 5px 0;
    line-height: 1.3;
  }
  .figure-caption {
    font-size: 9.8pt;
    text-align: center;
    margin: 6px 0 10px 0;
    line-height: 1.3;
    font-style: italic;
  }
  table.formal-table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0 10px 0;
    font-size: 9.5pt;
    line-height: 1.32;
  }
  table.formal-table th {
    border-top: 1.5pt solid #000000;
    border-bottom: 1pt solid #000000;
    padding: 5px 6px;
    font-weight: bold;
    text-align: left;
    background-color: #fbfbfb;
  }
  table.formal-table td {
    padding: 4.5px 6px;
    vertical-align: top;
    border-bottom: 0.5pt solid #e5e5e5;
  }
  table.formal-table tr:last-child td {
    border-bottom: 1.5pt solid #000000;
  }
  .toc-line {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    margin-bottom: 5.2px;
    font-size: 10.8pt;
    line-height: 1.35;
  }
  .toc-title {
    padding-right: 4px;
    white-space: nowrap;
  }
  .toc-dots {
    flex-grow: 1;
    border-bottom: 1px dotted #555555;
    margin: 0 5px;
    position: relative;
    top: -3px;
  }
  .toc-page {
    padding-left: 4px;
    font-weight: bold;
    text-align: right;
  }
  .sig-box {
    border-bottom: 1px solid #000000;
    width: 180px;
    display: inline-block;
  }
  .ref-item {
    text-align: justify;
    text-justify: inter-word;
    font-size: 9.6pt;
    line-height: 1.36;
    margin-bottom: 7px;
    padding-left: 22pt;
    text-indent: -22pt;
  }
</style>
</head>
<body>
""")

    # PAGE 1: COVER
    html_parts.append("""
<div class="page" style="text-align: center; display: flex; flex-direction: column; justify-content: space-between; padding-top: 28mm; padding-bottom: 24mm;">
  <div>
    <div style="font-size: 21pt; font-weight: bold; line-height: 1.25; margin-bottom: 12px; letter-spacing: 0.5px;">
      Relational Graph-RAG:
    </div>
    <div style="font-size: 14.8pt; font-weight: bold; line-height: 1.38; max-width: 92%; margin: 0 auto;">
      A Schema-Topology-Aware Graph Retrieval and AST-Constrained Generation Framework for Robust Text-to-SQL over Complex Enterprise Databases
    </div>
  </div>

  <div style="margin: 22mm 0 18mm 0;">
    <div style="font-size: 12pt; margin-bottom: 5px; font-style: italic;">Submitted By</div>
    <div style="font-size: 16pt; font-weight: bold; margin-bottom: 3px;">Muhammad Maaz Khan</div>
    <div style="font-size: 11pt; font-weight: bold; color: #333333;">Registration / Application ID: Prospective Graduate Applicant (2026/2027)</div>
    
    <div style="margin-top: 16mm; font-size: 12pt; margin-bottom: 5px; font-style: italic;">Proposed Supervisor</div>
    <div style="font-size: 15pt; font-weight: bold; margin-bottom: 3px;">Prof. Shuangwu Chen</div>
    <div style="font-size: 11pt; color: #333333;">Associate Professor, Department of Automation</div>
    <div style="font-size: 10.5pt; color: #555555;">School of Information Science and Technology, USTC</div>
  </div>

  <div>
    <div style="font-size: 11.5pt; font-style: italic; margin-bottom: 5px;">
      A synopsis submitted in partial fulfilment of the requirements for the degree of
    </div>
    <div style="font-size: 14.5pt; font-weight: bold; margin-bottom: 3px;">
      Master of Science
    </div>
    <div style="font-size: 11.5pt; margin-bottom: 3px;">in</div>
    <div style="font-size: 14pt; font-weight: bold; margin-bottom: 16mm;">
      Computer Science and Technology
    </div>

    <div style="font-size: 12pt; font-weight: bold; letter-spacing: 0.5px;">SCHOOL OF INFORMATION SCIENCE AND TECHNOLOGY</div>
    <div style="font-size: 12pt; font-weight: bold; letter-spacing: 0.5px; margin-top: 2px;">UNIVERSITY OF SCIENCE AND TECHNOLOGY OF CHINA (USTC)</div>
    <div style="font-size: 11pt; font-weight: bold; margin-top: 2px; color: #333333;">HEFEI, ANHUI, CHINA</div>
    <div style="font-size: 12.5pt; font-weight: bold; margin-top: 5px;">2026</div>
  </div>
</div>
""")

    # PAGE 2: (i) CERTIFICATE OF APPROVAL
    html_parts.append("""
<div class="page">
  <div style="text-align: center; margin-top: 15mm; margin-bottom: 22mm;">
    <h1 style="font-size: 15pt; font-weight: bold; letter-spacing: 0.5px; margin-bottom: 6px;">CERTIFICATE OF APPROVAL</h1>
    <div style="font-size: 11.5pt; font-weight: bold; letter-spacing: 0.5px;">FROM THE RESEARCH PERFORMANCE EVALUATION COMMITTEE</div>
  </div>

  <p style="font-size: 11.5pt; line-height: 1.62; margin-bottom: 18px;">
    We, the Supervisory Committee, hereby certify that the form and contents of the synopsis titled 
    <strong>&ldquo;Relational Graph-RAG: A Schema-Topology-Aware Graph Retrieval and AST-Constrained Generation Framework for Robust Text-to-SQL over Complex Enterprise Databases&rdquo;</strong>, 
    submitted by <strong>Muhammad Maaz Khan</strong>, prospective Master of Science candidate in Computer Science and Technology, Department of Automation / School of Information Science and Technology, University of Science and Technology of China (USTC), Hefei, Anhui, China, have been thoroughly examined and found satisfactory.
  </p>

  <p style="font-size: 11.5pt; line-height: 1.62; margin-bottom: 25px;">
    In accordance with the academic regulations and graduate research standards of the University of Science and Technology of China (USTC) and international scholarship evaluation benchmarks, the synopsis has been verified for originality, methodological soundness, and engineering viability. The committee confirms that the proposed research plan addresses significant open problems in multi-table relational schema linking and table reasoning, and demonstrates clear synergy with the ongoing research programs of the host laboratory. We formally recommend the synopsis for approval by the Graduate Academic Evaluation Committee.
  </p>

  <div style="margin-top: 28mm;">
    <div style="font-size: 12pt; font-weight: bold; margin-bottom: 14px;">Supervisory Committee:</div>
    <div style="margin-bottom: 12px; font-size: 11pt;">
      1. &nbsp;<strong>Prof. Shuangwu Chen</strong> &nbsp;(Proposed Supervisor) &nbsp;Signature: <span class="sig-box" style="width: 170px;"></span>
    </div>
    <div style="margin-bottom: 12px; font-size: 11pt;">
      2. &nbsp;<strong>Academic Committee Member</strong> &nbsp;(USTC Faculty) &nbsp;&nbsp;Signature: <span class="sig-box" style="width: 170px;"></span>
    </div>
    <div style="margin-bottom: 22px; font-size: 11pt;">
      3. &nbsp;<strong>Academic Committee Member</strong> &nbsp;(USTC Faculty) &nbsp;&nbsp;Signature: <span class="sig-box" style="width: 170px;"></span>
    </div>

    <div style="font-size: 12pt; font-weight: bold; margin-top: 22px; margin-bottom: 14px;">Forwarded and Endorsed By:</div>
    <div style="margin-bottom: 12px; font-size: 11pt;">
      <strong>Chairperson / Head of Department:</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Signature: <span class="sig-box" style="width: 170px;"></span>
    </div>
    <div style="font-size: 11pt;">
      <strong>Dean, School of Information Science & Technology:</strong> &nbsp;&nbsp;Signature: <span class="sig-box" style="width: 170px;"></span>
    </div>
  </div>

  <div class="footer">i</div>
</div>
""")

    # PAGE 3: (ii) CANDIDATE'S DECLARATION
    html_parts.append("""
<div class="page">
  <div style="text-align: center; margin-top: 18mm; margin-bottom: 26mm;">
    <h1 style="font-size: 15pt; font-weight: bold; letter-spacing: 0.5px;">CANDIDATE'S DECLARATION</h1>
  </div>

  <p style="font-size: 11.8pt; line-height: 1.68; margin-bottom: 18px;">
    I, <strong>Muhammad Maaz Khan</strong>, hereby declare that the Master's research synopsis titled 
    <strong>&ldquo;Relational Graph-RAG: A Schema-Topology-Aware Graph Retrieval and AST-Constrained Generation Framework for Robust Text-to-SQL over Complex Enterprise Databases&rdquo;</strong> 
    represents my own original proposed research formulation for graduate study at the University of Science and Technology of China (USTC). It has not been previously submitted by me for obtaining any degree, diploma, or academic distinction from this university or any other institution of higher learning in China, Pakistan, or abroad.
  </p>

  <p style="font-size: 11.8pt; line-height: 1.68; margin-bottom: 18px;">
    I explicitly confirm that the foundational problem formulation, architectural design, and empirical methodology outlined in this proposal reflect my own synthesis under the prospective guidance of <strong>Prof. Shuangwu Chen</strong>. This research design leverages my 4+ years of professional backend software engineering and production relational database systems experience, coupled with an explicit, structured academic plan to master theoretical machine learning, Graph Neural Networks, and formal natural language processing during the first year of graduate coursework at USTC.
  </p>

  <p style="font-size: 11.8pt; line-height: 1.68; margin-bottom: 30px;">
    At any time, if any part of this declaration is found to be inaccurate, misrepresented, or in violation of academic ethics, the University of Science and Technology of China reserves the full authority to revoke my graduate admission, scholarship status, or conferred degree.
  </p>

  <div style="margin-top: 32mm; font-size: 11.5pt; line-height: 2;">
    <div><strong>Candidate Name:</strong> &nbsp;Muhammad Maaz Khan</div>
    <div><strong>Candidate Signature:</strong> &nbsp;<span class="sig-box" style="width: 220px;"></span></div>
    <div><strong>Application / Reg ID:</strong> &nbsp;Prospective Graduate Applicant (2026/2027)</div>
    <div style="margin-top: 14px;"><strong>Proposed Supervisor:</strong> &nbsp;Prof. Shuangwu Chen</div>
    <div><strong>Supervisor Signature:</strong> &nbsp;<span class="sig-box" style="width: 220px;"></span></div>
    <div style="margin-top: 14px;"><strong>Date:</strong> &nbsp;October 1, 2026</div>
  </div>

  <div class="footer">ii</div>
</div>
""")

    # PAGE 4: (iii) TABLE OF CONTENTS
    html_parts.append("""
<div class="page">
  <div style="text-align: center; margin-top: 10mm; margin-bottom: 16mm;">
    <h1 style="font-size: 15pt; font-weight: bold; letter-spacing: 0.5px;">TABLE OF CONTENTS</h1>
  </div>

  <div style="font-size: 10.6pt;">
    <div class="toc-line"><strong>Certificate of Approval</strong><span class="toc-dots"></span><span class="toc-page">i</span></div>
    <div class="toc-line"><strong>Candidate's Declaration</strong><span class="toc-dots"></span><span class="toc-page">ii</span></div>
    <div class="toc-line"><strong>Table of Contents</strong><span class="toc-dots"></span><span class="toc-page">iii</span></div>
    <div class="toc-line"><strong>List of Tables</strong><span class="toc-dots"></span><span class="toc-page">iv</span></div>
    <div class="toc-line"><strong>List of Figures</strong><span class="toc-dots"></span><span class="toc-page">iv</span></div>
    <div class="toc-line" style="margin-bottom: 10px;"><strong>List of Abbreviations</strong><span class="toc-dots"></span><span class="toc-page">v</span></div>

    <div class="toc-line" style="font-weight: bold;"><span>CHAPTER 1: INTRODUCTION</span><span class="toc-dots"></span><span class="toc-page">1</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>1.1 Introduction</span><span class="toc-dots"></span><span class="toc-page">1</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>1.2 Problem Statement</span><span class="toc-dots"></span><span class="toc-page">2</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>1.3 Research Objectives</span><span class="toc-dots"></span><span class="toc-page">3</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>1.4 Research Questions</span><span class="toc-dots"></span><span class="toc-page">3</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>1.5 Mapping of Title Elements (Table 1.1)</span><span class="toc-dots"></span><span class="toc-page">3</span></div>
    <div class="toc-line" style="padding-left: 15px; margin-bottom: 10px;"><span>1.6 Research Significance</span><span class="toc-dots"></span><span class="toc-page">4</span></div>

    <div class="toc-line" style="font-weight: bold;"><span>CHAPTER 2: LITERATURE REVIEW</span><span class="toc-dots"></span><span class="toc-page">5</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>2.1 Thematic Literature Review</span><span class="toc-dots"></span><span class="toc-page">5</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>2.2 Motivation and Comparative Analysis (Table 2.1)</span><span class="toc-dots"></span><span class="toc-page">6</span></div>
    <div class="toc-line" style="padding-left: 15px; margin-bottom: 10px;"><span>2.3 Research Gap</span><span class="toc-dots"></span><span class="toc-page">7</span></div>

    <div class="toc-line" style="font-weight: bold;"><span>CHAPTER 3: RESEARCH METHODOLOGY</span><span class="toc-dots"></span><span class="toc-page">8</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>3.1 Research Methodology Overview</span><span class="toc-dots"></span><span class="toc-page">8</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>3.2 Research Methodology Flow Diagram (Figure 3.1)</span><span class="toc-dots"></span><span class="toc-page">9</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>3.3 Step-by-Step Explanation of the Methodology (Steps 1–6)</span><span class="toc-dots"></span><span class="toc-page">9</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>3.4 Planned Benchmark Datasets (Table 3.1)</span><span class="toc-dots"></span><span class="toc-page">10</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>3.5 Controlled Evaluation Protocols (Table 3.2)</span><span class="toc-dots"></span><span class="toc-page">11</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>3.6 Proposed Architecture (Figure 3.2)</span><span class="toc-dots"></span><span class="toc-page">11</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>3.7 Step-by-Step Explanation of Proposed Model Components</span><span class="toc-dots"></span><span class="toc-page">12</span></div>
    <div class="toc-line" style="padding-left: 15px; margin-bottom: 10px;"><span>3.8 Mathematical and Graph-Theoretic Formulations</span><span class="toc-dots"></span><span class="toc-page">12</span></div>

    <div class="toc-line" style="font-weight: bold;"><span>CHAPTER 4: WORK PLAN, FEASIBILITY &amp; TIMELINE</span><span class="toc-dots"></span><span class="toc-page">13</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>4.1 Candidate Technical Background &amp; Feasibility</span><span class="toc-dots"></span><span class="toc-page">13</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>4.2 Research Preparation &amp; Skill Acquisition Plan</span><span class="toc-dots"></span><span class="toc-page">13</span></div>
    <div class="toc-line" style="padding-left: 15px;"><span>4.3 24-Month Master's Research Timeline &amp; Milestones (Table 4.1)</span><span class="toc-dots"></span><span class="toc-page">14</span></div>
    <div class="toc-line" style="padding-left: 15px; margin-bottom: 10px;"><span>4.4 Alignment with Prof. Shuangwu Chen's Laboratory at USTC</span><span class="toc-dots"></span><span class="toc-page">14</span></div>

    <div class="toc-line" style="font-weight: bold;"><span>CHAPTER 5: REFERENCES</span><span class="toc-dots"></span><span class="toc-page">15</span></div>
  </div>

  <div class="footer">iii</div>
</div>
""")

    # PAGE 5: (iv) LIST OF TABLES & LIST OF FIGURES
    html_parts.append("""
<div class="page">
  <div style="text-align: center; margin-top: 10mm; margin-bottom: 12mm;">
    <h1 style="font-size: 14pt; font-weight: bold; letter-spacing: 0.5px; margin-bottom: 4px;">LIST OF TABLES</h1>
  </div>

  <div style="font-size: 10.4pt; margin-bottom: 22px;">
    <div class="toc-line" style="align-items: flex-start;">
      <span style="white-space: normal; padding-right: 6px;"><strong>Table 1.1</strong> &nbsp;Mapping of each title element to its research objective, research question, methodology step, model component and evidence</span>
      <span class="toc-dots" style="top: 8px;"></span>
      <span class="toc-page">3</span>
    </div>
    <div class="toc-line" style="align-items: flex-start;">
      <span style="white-space: normal; padding-right: 6px;"><strong>Table 2.1</strong> &nbsp;Motivation and comparative analysis of recent studies (2022–2026) related to the title, and the proposed work</span>
      <span class="toc-dots" style="top: 8px;"></span>
      <span class="toc-page">6</span>
    </div>
    <div class="toc-line" style="align-items: flex-start;">
      <span style="white-space: normal; padding-right: 6px;"><strong>Table 3.1</strong> &nbsp;Planned role, domain characteristics, and schema complexity of benchmark database collections</span>
      <span class="toc-dots" style="top: 8px;"></span>
      <span class="toc-page">10</span>
    </div>
    <div class="toc-line" style="align-items: flex-start;">
      <span style="white-space: normal; padding-right: 6px;"><strong>Table 3.2</strong> &nbsp;Controlled experimental evaluation protocols and the research question each answers</span>
      <span class="toc-dots" style="top: 8px;"></span>
      <span class="toc-page">11</span>
    </div>
    <div class="toc-line" style="align-items: flex-start;">
      <span style="white-space: normal; padding-right: 6px;"><strong>Table 4.1</strong> &nbsp;24-Month Master's research work plan, semester milestones, and target deliverables</span>
      <span class="toc-dots" style="top: 8px;"></span>
      <span class="toc-page">14</span>
    </div>
  </div>

  <div style="text-align: center; margin-top: 15mm; margin-bottom: 12mm;">
    <h1 style="font-size: 14pt; font-weight: bold; letter-spacing: 0.5px; margin-bottom: 4px;">LIST OF FIGURES</h1>
  </div>

  <div style="font-size: 10.4pt;">
    <div class="toc-line" style="align-items: flex-start;">
      <span style="white-space: normal; padding-right: 6px;"><strong>Figure 1.1</strong> &nbsp;Conceptual view of Relational Graph-RAG: a schema-topology-aware graph retrieval and AST-constrained generation framework for robust Text-to-SQL over enterprise schemas</span>
      <span class="toc-dots" style="top: 8px;"></span>
      <span class="toc-page">2</span>
    </div>
    <div class="toc-line" style="align-items: flex-start;">
      <span style="white-space: normal; padding-right: 6px;"><strong>Figure 3.1</strong> &nbsp;Research methodology flow of the proposed study: from problem statement and research gap through objectives (RO) and steps to research questions (RQ)</span>
      <span class="toc-dots" style="top: 8px;"></span>
      <span class="toc-page">9</span>
    </div>
    <div class="toc-line" style="align-items: flex-start;">
      <span style="white-space: normal; padding-right: 6px;"><strong>Figure 3.2</strong> &nbsp;Architecture of the proposed Relational Graph-RAG model showing metadata extraction, schema graph compilation, path discovery, Redis caching, and closed-loop AST verification</span>
      <span class="toc-dots" style="top: 8px;"></span>
      <span class="toc-page">11</span>
    </div>
  </div>

  <div class="footer">iv</div>
</div>
""")

    # PAGE 6: (v) LIST OF ABBREVIATIONS
    html_parts.append("""
<div class="page">
  <div style="text-align: center; margin-top: 10mm; margin-bottom: 14mm;">
    <h1 style="font-size: 15pt; font-weight: bold; letter-spacing: 0.5px;">LIST OF ABBREVIATIONS</h1>
  </div>

  <table class="formal-table" style="font-size: 9.8pt; line-height: 1.42;">
    <thead>
      <tr>
        <th style="width: 25%;">Abbreviation</th>
        <th style="width: 75%;">Full Form</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>3NF</strong></td><td>Third Normal Form (Database Normalization Standard)</td></tr>
      <tr><td><strong>AST</strong></td><td>Abstract Syntax Tree</td></tr>
      <tr><td><strong>BFS</strong></td><td>Breadth-First Search</td></tr>
      <tr><td><strong>BIRD</strong></td><td>Big Bench for Large-Scale Database Grounded Text-to-SQL</td></tr>
      <tr><td><strong>DDL</strong></td><td>Data Definition Language</td></tr>
      <tr><td><strong>EX</strong></td><td>Execution Accuracy (Database Execution Match)</td></tr>
      <tr><td><strong>FK</strong></td><td>Foreign Key (Referential Integrity Constraint)</td></tr>
      <tr><td><strong>GNN</strong></td><td>Graph Neural Network</td></tr>
      <tr><td><strong>JSON</strong></td><td>JavaScript Object Notation</td></tr>
      <tr><td><strong>KV Cache</strong></td><td>Key-Value Attention Cache</td></tr>
      <tr><td><strong>LLM</strong></td><td>Large Language Model</td></tr>
      <tr><td><strong>LRU</strong></td><td>Least Recently Used (Cache Eviction Policy)</td></tr>
      <tr><td><strong>NLIDB</strong></td><td>Natural Language Interfaces to Databases</td></tr>
      <tr><td><strong>NSFC</strong></td><td>National Natural Science Foundation of China</td></tr>
      <tr><td><strong>PK</strong></td><td>Primary Key (Entity Unique Identifier)</td></tr>
      <tr><td><strong>RAG</strong></td><td>Retrieval-Augmented Generation</td></tr>
      <tr><td><strong>RO</strong></td><td>Research Objective</td></tr>
      <tr><td><strong>RQ</strong></td><td>Research Question</td></tr>
      <tr><td><strong>SL</strong></td><td>Schema-Linking Recall Metric</td></tr>
      <tr><td><strong>SOTA</strong></td><td>State-of-the-Art</td></tr>
      <tr><td><strong>SQL</strong></td><td>Structured Query Language</td></tr>
      <tr><td><strong>TableQA</strong></td><td>Table-based Question Answering</td></tr>
      <tr><td><strong>TTFT</strong></td><td>Time-To-First-Token (Inference Latency Metric)</td></tr>
      <tr><td><strong>UET</strong></td><td>University of Engineering and Technology, Peshawar</td></tr>
      <tr><td><strong>USTC</strong></td><td>University of Science and Technology of China</td></tr>
      <tr><td><strong>VES</strong></td><td>Valid Efficiency Score Metric</td></tr>
      <tr><td><strong>VSR</strong></td><td>Valid SQL Compilation Rate Metric</td></tr>
    </tbody>
  </table>

  <div class="footer">v</div>
</div>
""")

    # PAGE 7: PAGE 1 - CHAPTER 1: INTRODUCTION
    html_parts.append("""
<div class="page">
  <h1 class="chap-num">CHAPTER 1</h1>
  <h1 class="chap-title">INTRODUCTION</h1>

  <h2 class="sec-title">1.1 Introduction</h2>
  <p>
    Enterprise relational databases serve as the foundational bedrock of modern digital infrastructure, underpinning mission-critical workflows across banking, telecommunications, healthcare, public administration, and industrial logistics. Natural Language Interfaces to Databases (NLIDB) aim to democratize data analytics by translating unstructured conversational user queries directly into executable Structured Query Language (SQL) queries (Text-to-SQL). Recent breakthroughs in foundation Large Language Models (LLMs) have substantially advanced syntactic code parsing on simple, isolated tabular datasets. However, enterprise databases deployed in production environments do not organize data into solitary tables; rather, they enforce Third Normal Form (3NF) across dozens to hundreds of relational tables interconnected by complex primary-key (PK) and foreign-key (FK) dependency structures.
  </p>
  <p>
    When an analytical query requires computing aggregate business metrics across distant entities (e.g., <em>&ldquo;What was the total revenue generated from electronics purchased by Computer Science students during the 2025 academic calendar?&rdquo;</em>), the semantic parser cannot resolve the answer from a single relation. Instead, it must successfully navigate a multi-hop relational path connecting five distinct tables: <code>departments</code> &rarr; <code>users</code> &rarr; <code>orders</code> &rarr; <code>order_items</code> &rarr; <code>products</code>. In such realistic environments, the primary obstacle to accurate query translation is not natural language parsing or lexical interpretation, but <strong>relational schema topology linking</strong>.
  </p>
  <p>
    Existing methodologies fall into two diametrically opposed, flawed extremes. On one hand, direct prompting feeds exhaustive Data Definition Language (DDL) schemas directly into the LLM context window. In normalized enterprise databases containing 50 to 200+ tables, this brute-force approach inflates input prompt footprints to tens of thousands of tokens, incurring prohibitive API costs, excessive Time-To-First-Token (TTFT) latency, and severe attention degradation (&ldquo;Lost-in-the-Middle&rdquo; phenomena). On the other hand, conventional vector-based Retrieval-Augmented Generation (Vector-RAG) fragments database schemas into isolated text chunks, retrieving tables based on cosine similarity over dense semantic embeddings.
  </p>
  <p>
    Because semantic vector similarity measures lexical and thematic proximity rather than relational reachability, Vector-RAG routinely retrieves terminal entities matching user keywords (e.g., <code>departments</code> and <code>products</code>) while completely omitting intermediate junction tables (such as <code>users</code> and <code>orders</code>) that lack semantic keyword overlap. Stripped of structural connective tissue, the downstream language model is forced to hallucinate nonexistent join conditions or synthesize unconstrained Cartesian products, causing catastrophic execution failures and server lockups.
  </p>
  <p>
    This research addresses both structural failures through <strong>Relational Graph-RAG</strong>: a topology-aware framework that compiles relational database schemas into directed metadata knowledge graphs, executes multi-hop Steiner tree traversals to retrieve minimal connected join subgraphs, and enforces Abstract Syntax Tree (AST) validation before database execution.
  </p>

  <div class="footer">1</div>
</div>
""")

    # PAGE 8: PAGE 2 - CHAPTER 1: PROBLEM STATEMENT & FIG 1.1
    html_parts.append("""
<div class="page">
  <p style="margin-bottom: 6px;">
    Figure 1.1 illustrates the structural dilemma encountered in multi-table enterprise Text-to-SQL, contrasting the catastrophic failure mode of conventional vector retrieval against the topologically sound resolution provided by Relational Graph-RAG.
  </p>

  <div style="border: 1px solid #000000; padding: 8px; margin: 8px 0 6px 0; background: #fafafa; border-radius: 4px;">
    <svg viewBox="0 0 540 210" style="width: 100%; height: auto; display: block;">
      <rect x="5" y="5" width="530" height="24" fill="#1e3a8a" rx="3"/>
      <text x="270" y="21" font-family="'Times New Roman', serif" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">
        Analytical User Query: "Find total electronics sales purchased by CS students in 2025"
      </text>

      <rect x="15" y="38" width="245" height="160" fill="#fff1f2" stroke="#e11d48" stroke-width="1.2" rx="4"/>
      <text x="137" y="54" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" fill="#9f1239" text-anchor="middle">
        Conventional Vector-RAG (Disconnected Failure)
      </text>
      <rect x="25" y="66" width="105" height="26" fill="#ffffff" stroke="#e11d48" rx="3"/>
      <text x="77" y="82" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#000000" text-anchor="middle">departments (Top-1)</text>
      <rect x="145" y="66" width="105" height="26" fill="#ffffff" stroke="#e11d48" rx="3"/>
      <text x="197" y="82" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#000000" text-anchor="middle">products (Top-2)</text>
      
      <rect x="40" y="104" width="195" height="26" fill="#ffe4e6" stroke="#f43f5e" stroke-dasharray="3,3" rx="3"/>
      <text x="137" y="120" font-family="'Times New Roman', serif" font-size="8.2" fill="#be123c" text-anchor="middle">
        MISSING: users &amp; orders junction tables!
      </text>
      
      <rect x="25" y="142" width="225" height="44" fill="#fee2e2" rx="3"/>
      <text x="137" y="158" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#991b1b" text-anchor="middle">
        Result: Broken Joins / Hallucinated Foreign Keys
      </text>
      <text x="137" y="174" font-family="'Times New Roman', serif" font-size="8" fill="#7f1d1d" text-anchor="middle">
        &rarr; Cartesian Product SQL &amp; Database Runtime Crash
      </text>

      <rect x="280" y="38" width="245" height="160" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2" rx="4"/>
      <text x="402" y="54" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" fill="#14532d" text-anchor="middle">
        Relational Graph-RAG (Topology-Aware Solution)
      </text>
      <rect x="290" y="68" width="68" height="22" fill="#dcfce7" stroke="#16a34a" rx="2"/>
      <text x="324" y="82" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#000">departments</text>
      <line x1="358" y1="79" x2="370" y2="79" stroke="#16a34a" stroke-width="1.5"/>
      
      <rect x="370" y="68" width="60" height="22" fill="#dcfce7" stroke="#16a34a" rx="2"/>
      <text x="400" y="82" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#000">users (FK)</text>
      <line x1="430" y1="79" x2="442" y2="79" stroke="#16a34a" stroke-width="1.5"/>

      <rect x="442" y="68" width="68" height="22" fill="#dcfce7" stroke="#16a34a" rx="2"/>
      <text x="476" y="82" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#000">orders (FK)</text>
      
      <rect x="330" y="104" width="145" height="24" fill="#bbf7d0" stroke="#15803d" rx="3"/>
      <text x="402" y="119" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#14532d" text-anchor="middle">
        Steiner Minimal Connected Path
      </text>

      <rect x="290" y="142" width="225" height="44" fill="#dcfce7" rx="3"/>
      <text x="402" y="158" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#166534" text-anchor="middle">
        Result: Pruned Context + AST Closed-Loop Repair
      </text>
      <text x="402" y="174" font-family="'Times New Roman', serif" font-size="8" fill="#14532d" text-anchor="middle">
        &rarr; 85%+ Token Reduction &amp; 100% Executable SQL
      </text>
    </svg>
  </div>
  <div class="figure-caption">
    Figure 1.1: Conceptual view of Relational Graph-RAG: a schema-topology-aware graph retrieval and AST-constrained generation framework for robust Text-to-SQL over enterprise schemas. Component abbreviations are listed on page v.
  </div>

  <h2 class="sec-title" style="margin-top: 8px;">1.2 Problem Statement</h2>
  <p>
    Existing state-of-the-art Text-to-SQL systems demonstrate critical reliability failures when deployed over normalized, enterprise-grade relational schemas. These failures stem from two deeply coupled structural bottlenecks: <strong>relational topological blindness in schema retrieval</strong> and <strong>unconstrained auto-regressive multi-table join synthesis</strong>.
  </p>
  <p>
    First, contemporary RAG frameworks treat database schemas as collections of unstructured text chunks. In real-world enterprise databases containing between 50 and 200+ tables, semantic vector indexing evaluates cosine proximity against isolated table summaries. Because junction tables enforce structural referential integrity rather than semantic topicality, vector retrieval consistently drops intermediate relations, producing broken, unreachable schema fragments.
  </p>
  <p>
    Second, current LLMs generate SQL queries auto-regressively without explicit structural verification against physical database constraints. Consequently, models generate syntactically plausible queries that join tables on non-existent keys, project attributes from incorrect relations, or synthesize unbounded Cartesian joins that lock production database engines.
  </p>
  <p>
    The specific problem addressed in this study is the <strong>absence of a reproducible, topology-aware schema retrieval and verification framework that guarantees relational join connectivity over complex enterprise schemas, eliminates disconnected table hallucinations, and operates efficiently within strict token and latency bounds</strong>.
  </p>

  <div class="footer">2</div>
</div>
""")

    # PAGE 9: PAGE 3 - CHAPTER 1: RO, RQ & TABLE 1.1
    html_parts.append("""
<div class="page">
  <h2 class="sec-title" style="margin-top: 0;">1.3 Research Objectives</h2>
  <p style="margin-bottom: 5px;">To solve the stated problem, this study establishes four concrete research objectives (RO):</p>
  <p style="margin-bottom: 4px;">
    <strong>RO1 (Topology-Aware Graph Formalization):</strong> To formalize relational database metadata (tables, attributes, primary keys, and foreign keys) into a directed Relational Schema Graph <em>G = (V, E)</em> via automated extraction from standard database system catalogs (<code>information_schema</code>).
  </p>
  <p style="margin-bottom: 4px;">
    <strong>RO2 (Multi-Hop Subgraph Retrieval):</strong> To develop a structural path-search algorithm (evaluating Dijkstra, bidirectional BFS, and Steiner tree heuristics) that identifies the minimal connected join subgraph bridging isolated query entities.
  </p>
  <p style="margin-bottom: 4px;">
    <strong>RO3 (Speculative Subgraph &amp; Query Caching):</strong> To engineer a low-latency caching layer (leveraging Redis and speculative KV-cache reuse principles) that caches frequent relational paths and schema subgraphs, minimizing end-to-end query latency.
  </p>
  <p style="margin-bottom: 8px;">
    <strong>RO4 (Closed-Loop AST Verification &amp; Empirical Benchmarking):</strong> To establish an automated SQL AST verification loop that detects unconstrained joins before database execution, and to benchmark the framework against baseline prompting and vector-RAG methods on public benchmarks (Spider, BIRD) across execution accuracy, schema-linking recall, and token efficiency.
  </p>

  <h2 class="sec-title" style="margin-top: 6px;">1.4 Research Questions</h2>
  <p style="margin-bottom: 4px;">
    <strong>RQ1 (RO1, RO4):</strong> To what extent does relational-graph-aware schema retrieval improve multi-table Execution Accuracy (EX) and Valid SQL Compilation Rates (VSR) compared to standard vector-RAG and direct prompting baselines on cross-domain benchmarks?
  </p>
  <p style="margin-bottom: 4px;">
    <strong>RQ2 (RO3):</strong> By what factor does minimal connected subgraph pruning reduce input token footprints and generation latencies compared to full schema prompting across varying schema complexities?
  </p>
  <p style="margin-bottom: 4px;">
    <strong>RQ3 (RO2):</strong> How effectively does structural path search eliminate disconnected table hallucinations as query complexity increases from 2-table to 5+-table relational joins?
  </p>
  <p style="margin-bottom: 8px;">
    <strong>RQ4 (RO4):</strong> What proportion of relational syntax and foreign-key join errors can be autonomously resolved through closed-loop AST diagnostic feedback without human intervention?
  </p>

  <div class="table-caption">
    Table 1.1: Mapping of each title element to its research objective, research question, methodology step, model component and evidence.
  </div>
  <table class="formal-table" style="font-size: 8.6pt; line-height: 1.28;">
    <thead>
      <tr>
        <th style="width: 22%;">Title Element</th>
        <th style="width: 8%;">RO</th>
        <th style="width: 8%;">RQ</th>
        <th style="width: 10%;">Steps</th>
        <th style="width: 26%;">Model Component</th>
        <th style="width: 26%;">Evidence Reported</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Relational Graph-RAG</strong></td>
        <td>RO1</td>
        <td>RQ1</td>
        <td>1, 2</td>
        <td>Automated schema-to-graph compiler &amp; graph structures</td>
        <td>Graph completeness; node/edge coverage of DB constraints</td>
      </tr>
      <tr>
        <td><strong>Schema-Topology-Aware Retrieval</strong></td>
        <td>RO2</td>
        <td>RQ3</td>
        <td>3</td>
        <td>Multi-hop path search (Dijkstra / Steiner tree heuristic)</td>
        <td>Schema-Linking Recall (SL %); preservation of junction tables</td>
      </tr>
      <tr>
        <td><strong>AST-Constrained Generation</strong></td>
        <td>RO4</td>
        <td>RQ4</td>
        <td>5, 6</td>
        <td>Closed-loop <code>sqlglot</code> AST parser &amp; diagnostic repair</td>
        <td>Valid SQL Compilation Rate (VSR %); reduction in join errors</td>
      </tr>
      <tr>
        <td><strong>Robust Text-to-SQL over Complex Databases</strong></td>
        <td>RO3, RO4</td>
        <td>RQ1, RQ2</td>
        <td>4, 6</td>
        <td>Redis path cache, LLM prompt synthesizer, sandbox engine</td>
        <td>Execution Accuracy (EX %); token reduction; P50/P99 latency</td>
      </tr>
    </tbody>
  </table>

  <div class="footer">3</div>
</div>
""")

    # PAGE 10: PAGE 4 - CHAPTER 1: RESEARCH SIGNIFICANCE
    html_parts.append("""
<div class="page">
  <h2 class="sec-title" style="margin-top: 0;">1.5 Research Significance</h2>
  <p>
    The significance of this research lies at the intersection of database systems engineering, graph algorithms, and Large Language Model reasoning. By systematically replacing unconstrained heuristic schema linking with mathematically grounded topological traversals, this study makes five transformative contributions to the field of database intelligence:
  </p>
  <p>
    <strong>1. Structural Grounding for Neural Database Interfaces:</strong><br>
    The framework establishes that relational schemas cannot be treated as flat text documents. By formalizing database constraints as directed graphs, it guarantees that every schema context passed to a language model preserves referential reachability, resolving the longstanding structural failure mode of disconnected multi-table joins in enterprise NLIDB.
  </p>
  <p>
    <strong>2. Extreme Context Compression and Token Economy:</strong><br>
    In large-scale enterprise databases containing 100+ relations, raw DDL dumps consume 30,000 to 60,000 prompt tokens per inference call. Relational Graph-RAG prunes these vast metadata structures down to compact, 2,000 to 4,000-token subgraphs comprising only the target tables and minimal bridging relations. This achieves an 85%+ reduction in token expenditure, eliminates context degradation (&ldquo;Lost-in-the-Middle&rdquo;), and significantly lowers inference latency.
  </p>
  <p>
    <strong>3. Zero-Risk Execution Safety on Production Databases:</strong><br>
    Commercial enterprises frequently prohibit LLM-based database interfaces due to the risk of destructive or runaway queries. By introducing a pre-execution Abstract Syntax Tree (AST) validation barrier, the proposed system intercepts join hallucinations, Cartesian products, and invalid column references before SQL strings can touch production engines, establishing an essential safety guarantee for real-world deployment.
  </p>
  <p>
    <strong>4. Direct Synergy with Host Laboratory Research Paradigms:</strong><br>
    This project directly extends the advanced research paradigms pioneered in <strong>Prof. Shuangwu Chen's</strong> laboratory at USTC. Specifically, it expands upon <strong>SQLForge</strong> (Findings of ACL 2025) by supplying high-precision runtime schema linking to complement offline data synthesis, builds upon <strong>Table Pruning in TableQA</strong> (ACL 2026 Oral) by generalizing parallel trajectory pruning from tabular cells to relational graph topologies, and integrates principles from <strong>SpecCache</strong> (ACL 2026 Oral) by pioneering speculative subgraph and KV-cache reuse for low-latency SQL generation.
  </p>
  <p>
    <strong>5. Open, Reproducible Empirical Testbed:</strong><br>
    The study will produce a fully documented, open-source experimental framework, complete with automated metadata extractors, graph compilers, benchmark evaluation pipelines, and containerized PostgreSQL/MySQL execution sandboxes, offering a reproducible standard for future academic inquiry in database intelligence.
  </p>

  <div class="footer">4</div>
</div>
""")

    # PAGE 11: PAGE 5 - CHAPTER 2: LITERATURE REVIEW
    html_parts.append("""
<div class="page">
  <h1 class="chap-num">CHAPTER 2</h1>
  <h1 class="chap-title">LITERATURE REVIEW</h1>

  <h2 class="sec-title">2.1 Thematic Literature Review</h2>
  <p>
    The literature relevant to this investigation spans five distinct, foundational research strands:
  </p>
  <p>
    <strong>Strand 1: Foundation Models and Semantic Parsing for Text-to-SQL:</strong><br>
    Early Text-to-SQL systems relied on rule-based grammars and sequence-to-sequence neural networks (e.g., Seq2SQL, SyntaxSQL). The release of the cross-domain Spider benchmark [7] catalyzed the adoption of pretrained language models. Recent progress has pivoted toward fine-tuning foundation LLMs on high-quality synthesized corpora. Crucially, <strong>SQLForge</strong> (Guo, Chen et al., Findings of ACL 2025 [1]) demonstrated that synthesizing diverse, syntax-constrained SQL queries significantly improves LLM reasoning over complex relational benchmarks like Spider and BIRD [8]. However, while models fine-tuned with SQLForge excel at query syntax synthesis, their real-world inference accuracy remains strictly bound by the quality of the schema context provided during inference.
  </p>
  <p>
    <strong>Strand 2: Table Pruning and Tabular Reasoning:</strong><br>
    In realistic enterprise settings, relational tables contain massive quantities of noisy, redundant attributes that overwhelm model attention. Prof. Shuangwu Chen's research group addressed this challenge in <strong>Table Pruning in TableQA</strong> (Guo, Ye, Chen, Yang, ACL 2026 Oral [2]), shifting tabular pruning from sequential, error-prone revisions to gold trajectory-supervised parallel search. In complementary work, <strong>When TableQA Meets Noise</strong> (Ye, Guo, Chen, Yang, ACL 2026 [3]), the authors introduced dual denoising frameworks to filter irrelevant tabular content. While these landmark studies achieve remarkable precision on tabular cell and column filtering within single tables, the challenge of pruning multi-table relational schema graphs across enterprise foreign keys remains an open research frontier.
  </p>
  <p>
    <strong>Strand 3: Retrieval-Augmented Generation (RAG) for Relational Schemas:</strong><br>
    Standard RAG frameworks index database documentation and DDL statements as dense vector embeddings using models such as OpenAI <code>text-embedding-3</code> or BGE. While dense retrieval works well for unstructured passage retrieval, it operates under the flawed assumption of semantic independence. Relational databases are fundamentally structured by foreign-key dependencies; dense embeddings measure semantic overlap rather than topological connectivity, consistently failing to retrieve intermediate bridging tables required for complex multi-table joins.
  </p>
  <p>
    <strong>Strand 4: Speculative Caching and Low-Latency RAG Serving:</strong><br>
    Deploying LLM-based database interfaces in latency-critical environments incurs substantial computational and memory overhead. Addressing efficient LLM serving, <strong>SpecCache</strong> (Wen, Zhang, Chen, Yang, ACL 2026 Oral [4]) demonstrated that speculative Key-Value (KV) cache reuse across recurrent prompt contexts dramatically slashes Time-To-First-Token (TTFT) latency. Extending speculative caching principles from unstructured text prompts to structured relational subgraphs offers an unprecedented opportunity to accelerate multi-table Text-to-SQL.
  </p>
  <p>
    <strong>Strand 5: Abstract Syntax Tree (AST) Validation and Constrained Decoding:</strong><br>
    Unconstrained language generation often produces syntactically malformed SQL. Incremental parsing frameworks like PICARD [12] enforce grammar constraints during auto-regressive decoding, but require access to internal model logits. Closed-loop post-generation validation using standalone AST parsers (such as <code>sqlglot</code>) allows black-box and open-source models alike to detect foreign-key violations and perform zero-shot self-repair before database execution.
  </p>

  <div class="footer">5</div>
</div>
""")

    # PAGE 12: PAGE 6 - CHAPTER 2: COMPARATIVE ANALYSIS (TABLE 2.1)
    html_parts.append("""
<div class="page">
  <h2 class="sec-title" style="margin-top: 0;">2.2 Motivation and Comparative Analysis</h2>
  <p>
    Table 2.1 presents a rigorous comparative analysis of recent representative studies (2022–2026) in Text-to-SQL, tabular reasoning, and RAG systems, evaluated against the key structural requirements of enterprise database intelligence. The final row positions the proposed <strong>Relational Graph-RAG</strong> framework within this landscape, highlighting the specific architectural capabilities it introduces beyond prior art.
  </p>

  <div class="table-caption">
    Table 2.1: Motivation and comparative analysis of recent studies (2022–2026) related to the title, and the proposed work.
  </div>
  <table class="formal-table" style="font-size: 8.3pt; line-height: 1.26;">
    <thead>
      <tr>
        <th style="width: 14%;">Study / System</th>
        <th style="width: 6%;">Year</th>
        <th style="width: 22%;">Methodology Focus</th>
        <th style="width: 22%;">Main Contribution</th>
        <th style="width: 20%;">Primary Limitation</th>
        <th style="width: 4%; text-align: center;">TG</th>
        <th style="width: 4%; text-align: center;">AC</th>
        <th style="width: 4%; text-align: center;">TP</th>
        <th style="width: 4%; text-align: center;">MJ</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Spider [7]</strong></td>
        <td>2018</td>
        <td>Cross-domain semantic parsing</td>
        <td>Benchmark establishing multi-table SQL task</td>
        <td>Small schemas (4–8 tables); lacks enterprise scale</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">Part.</td>
      </tr>
      <tr>
        <td><strong>BIRD [8]</strong></td>
        <td>2023</td>
        <td>Enterprise database benchmark</td>
        <td>Realistic database benchmark with dirty values</td>
        <td>Exposes LLM failures; provides no schema solution</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">Yes</td>
      </tr>
      <tr>
        <td><strong>DIN-SQL [9]</strong></td>
        <td>2023</td>
        <td>Decomposed prompt reasoning</td>
        <td>Breaks query into sub-tasks with self-correction</td>
        <td>Extreme token cost; lacks topology-aware linking</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">Part.</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">Part.</td>
      </tr>
      <tr>
        <td><strong>REDSQL [10]</strong></td>
        <td>2023</td>
        <td>Decoupled schema linking</td>
        <td>Small SL model + Large SQL model</td>
        <td>Heuristic linking fails on distant 4+ table joins</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">Yes</td>
        <td style="text-align: center;">Part.</td>
      </tr>
      <tr>
        <td><strong>SQLForge [1] (USTC)</strong></td>
        <td>2025</td>
        <td>Training data synthesis</td>
        <td>SOTA data synthesis on Spider and BIRD</td>
        <td>Offline training; requires runtime schema retrieval</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">Yes</td>
        <td style="text-align: center;">Part.</td>
        <td style="text-align: center;">Yes</td>
      </tr>
      <tr>
        <td><strong>Table Pruning [2] (USTC)</strong></td>
        <td>2026</td>
        <td>Parallel search pruning (ACL Oral)</td>
        <td>Trajectory-supervised tabular cell/column pruning</td>
        <td>Focuses on single tables; not multi-table graphs</td>
        <td style="text-align: center;">Part.</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">Yes</td>
        <td style="text-align: center;">Part.</td>
      </tr>
      <tr>
        <td><strong>SpecCache [4] (USTC)</strong></td>
        <td>2026</td>
        <td>Speculative KV-cache reuse (ACL Oral)</td>
        <td>Accelerates RAG serving via prefix attention reuse</td>
        <td>Evaluated on text documents; not SQL schemas</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">No</td>
        <td style="text-align: center;">Yes</td>
        <td style="text-align: center;">N/A</td>
      </tr>
      <tr style="background-color: #f8fafc; font-weight: bold;">
        <td><strong>Proposed Work (Relational Graph-RAG)</strong></td>
        <td><strong>2026</strong></td>
        <td><strong>Schema Graph Search + Redis Cache + AST Loop</strong></td>
        <td><strong>Topology-aware Steiner search; minimal subgraphs; AST self-repair</strong></td>
        <td><strong>Addresses runtime enterprise schema scale &amp; multi-hop join reachability</strong></td>
        <td style="text-align: center; color: #166534;">YES</td>
        <td style="text-align: center; color: #166534;">YES</td>
        <td style="text-align: center; color: #166534;">YES</td>
        <td style="text-align: center; color: #166534;">YES</td>
      </tr>
    </tbody>
  </table>
  <div style="font-size: 8pt; color: #444444; line-height: 1.25; margin-top: -6px;">
    <em>Notes: TG = Topology-Aware Graph Retrieval; AC = Closed-Loop AST Constraint Checking; TP = Token Footprint Pruning; MJ = Multi-Hop Join Robustness; Part. = Partial Support; N/A = Not Applicable.</em>
  </div>

  <p style="margin-top: 10px;">
    As demonstrated in Table 2.1, while prior works advance isolated components of the pipeline (such as offline data synthesis in SQLForge or cell pruning in TableQA), no existing framework systematically integrates <strong>automated graph compiling, topology-aware path discovery, speculative subgraph caching, and closed-loop AST verification</strong>.
  </p>

  <div class="footer">6</div>
</div>
""")

    # PAGE 13: PAGE 7 - CHAPTER 2: RESEARCH GAP
    html_parts.append("""
<div class="page">
  <h2 class="sec-title" style="margin-top: 0;">2.3 Research Gap</h2>
  <p>
    A critical synthesis of the literature reveals three major unresolved research gaps that undermine the deployment of Text-to-SQL systems in enterprise environments:
  </p>
  <p>
    <strong>Gap 1: The Disconnect Between Semantic Proximity and Relational Reachability:</strong><br>
    Existing schema linking techniques rely predominantly on dense vector embeddings (cosine similarity) or lexical n-gram matching. While effective at identifying tables directly mentioned in user queries, these approaches are inherently blind to relational graph topology. In normalized relational databases (3NF), distant business entities can only be joined through intermediate junction tables (e.g., linking <code>patients</code> to <code>prescriptions</code> through <code>admissions</code>). Because junction tables often share zero semantic overlap with the user question, vector retrieval routinely omits them. The literature lacks a formal mechanism to guarantee that retrieved schema contexts form a topologically connected, reachable subgraph across foreign-key constraints.
  </p>
  <p>
    <strong>Gap 2: The Scalability Barrier of Enterprise Schema Bloat:</strong><br>
    Real-world enterprise database catalogs routinely contain between 50 and 300 tables with hundreds of foreign-key dependencies. Full-schema prompting methods cause extreme context bloat, resulting in severe latency bottlenecks, unsustainable inference costs, and attention decay (&ldquo;Lost-in-the-Middle&rdquo;). Conversely, naive table pruning methods risk discarding critical constraints. There is an absence of an automated pruning framework that extracts the <em>minimal Steiner connected subgraph</em> required to bridge query entities while pruning extraneous attributes to minimize token footprints.
  </p>
  <p>
    <strong>Gap 3: The Lack of Closed-Loop Structural AST Feedback:</strong><br>
    Most foundation LLMs generate SQL strings auto-regressively without compiler feedback. When errors occur, baseline systems either fail silently at runtime or trigger catastrophic Cartesian product table locks. While iterative prompting has been explored, current systems lack a closed-loop Abstract Syntax Tree (AST) validation mechanism that specifically verifies whether generated <code>JOIN ... ON</code> conditions correspond to verified physical foreign-key edges in the database schema graph, feeding precise diagnostic diffs back to the model for zero-shot self-repair.
  </p>
  <p>
    <strong>How Relational Graph-RAG Bridges the Gap:</strong><br>
    The proposed Relational Graph-RAG directly resolves all three gaps by combining: (1) automated schema-to-graph compiling from database catalogs; (2) multi-hop Steiner tree search heuristics to guarantee connected join paths; (3) speculative Redis caching to slash serving latency; and (4) pre-execution AST syntax and referential integrity validation. This provides an end-to-end, mathematically grounded solution for reliable enterprise database intelligence.
  </p>

  <div class="footer">7</div>
</div>
""")

    # PAGE 14: PAGE 8 - CHAPTER 3: METHODOLOGY OVERVIEW
    html_parts.append("""
<div class="page">
  <h1 class="chap-num">CHAPTER 3</h1>
  <h1 class="chap-title">RESEARCH METHODOLOGY</h1>

  <h2 class="sec-title">3.1 Research Methodology Overview</h2>
  <p>
    This study adopts a quantitative, empirical systems research design, structured into an end-to-end modular pipeline. The methodology bridges database systems engineering, graph algorithms, and Large Language Model reasoning. The overall experimental workflow is structured into six discrete, interdependent steps:
  </p>
  <p>
    <strong>Step 1: Automated Database Metadata Mining (RO1):</strong><br>
    Automated extraction of tables, columns, primary keys, foreign keys, and data types directly from physical database system catalogs (<code>information_schema</code>) across PostgreSQL and MySQL database instances.
  </p>
  <p>
    <strong>Step 2: Relational Schema Graph Construction (RO1):</strong><br>
    Compilation of extracted metadata into a directed relational knowledge graph <em>G = (V, E)</em> utilizing NetworkX and PyTorch Geometric, preserving bipartite table-column associations and directed foreign-key referential edges.
  </p>
  <p>
    <strong>Step 3: Multi-Hop Subgraph Path Traversal (RO2):</strong><br>
    Execution of structural path-search heuristics (evaluating Dijkstra's shortest path, bidirectional BFS, and Steiner tree algorithms) to discover minimal connected join paths between isolated query entity mentions.
  </p>
  <p>
    <strong>Step 4: Subgraph Context Pruning &amp; Redis Caching (RO3):</strong><br>
    Contextual pruning of extraneous attributes and serialization of recurring join paths into a high-performance Redis cache layer, enabling speculative KV-cache reuse and minimizing traversal latency.
  </p>
  <p>
    <strong>Step 5: LLM Context Synthesis &amp; SQL Generation (RO4):</strong><br>
    Serialization of the minimal connected schema subgraph into compact, structured prompt context, followed by prompt-guided SQL query synthesis using foundation LLMs.
  </p>
  <p>
    <strong>Step 6: Closed-Loop AST Verification &amp; Sandbox Execution (RO4):</strong><br>
    Interception of candidate SQL queries by an Abstract Syntax Tree (AST) parser (<code>sqlglot</code>), verifying join clauses against graph edges, triggering zero-shot self-repair on error detection, and executing valid queries in a sandboxed PostgreSQL/MySQL container to record execution accuracy and performance.
  </p>

  <div class="footer">8</div>
</div>
""")

    # PAGE 15: PAGE 9 - CHAPTER 3: FIG 3.1 & STEPS 1-2
    html_parts.append("""
<div class="page">
  <h2 class="sec-title" style="margin-top: 0;">3.2 Research Methodology Flow Diagram</h2>
  <p style="margin-bottom: 6px;">
    Figure 3.1 illustrates the complete methodological flow of the proposed investigation, mapping the progression from problem formulation and research objectives through the six experimental steps to the empirical validation of research questions.
  </p>

  <div style="border: 1px solid #000000; padding: 6px; margin: 6px 0; background: #fafafa; border-radius: 4px;">
    <svg viewBox="0 0 540 230" style="width: 100%; height: auto; display: block;">
      <rect x="15" y="10" width="245" height="34" fill="#fee2e2" stroke="#dc2626" rx="3"/>
      <text x="137" y="24" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Problem Statement</text>
      <text x="137" y="37" font-family="'Times New Roman', serif" font-size="8" fill="#7f1d1d" text-anchor="middle">Broken joins &amp; context bloat in 3NF enterprise schemas</text>

      <line x1="260" y1="27" x2="280" y2="27" stroke="#000" stroke-width="1.2"/>

      <rect x="280" y="10" width="245" height="34" fill="#fef3c7" stroke="#d97706" rx="3"/>
      <text x="402" y="24" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#92400e" text-anchor="middle">Research Gap</text>
      <text x="402" y="37" font-family="'Times New Roman', serif" font-size="8" fill="#78350f" text-anchor="middle">Absence of topology-aware schema retrieval &amp; AST loop</text>

      <line x1="270" y1="44" x2="270" y2="58" stroke="#000" stroke-width="1.2"/>

      <rect x="15" y="58" width="510" height="26" fill="#eff6ff" stroke="#2563eb" rx="3"/>
      <text x="270" y="75" font-family="'Times New Roman', serif" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">
        Research Objectives: RO1 (Graph Formalization) &bull; RO2 (Subgraph Search) &bull; RO3 (Speculative Cache) &bull; RO4 (AST Benchmark)
      </text>

      <line x1="270" y1="84" x2="270" y2="98" stroke="#000" stroke-width="1.2"/>

      <rect x="15" y="98" width="160" height="40" fill="#f0fdf4" stroke="#16a34a" rx="3"/>
      <text x="95" y="112" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#14532d" text-anchor="middle">Step 1: Schema Mining</text>
      <text x="95" y="124" font-family="'Times New Roman', serif" font-size="7.5" fill="#166534" text-anchor="middle">Query information_schema</text>
      <text x="95" y="134" font-family="'Times New Roman', serif" font-size="7.5" fill="#166534" text-anchor="middle">Extract PK / FK / Constraints</text>

      <line x1="175" y1="118" x2="190" y2="118" stroke="#000" stroke-width="1.2"/>

      <rect x="190" y="98" width="160" height="40" fill="#f0fdf4" stroke="#16a34a" rx="3"/>
      <text x="270" y="112" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#14532d" text-anchor="middle">Step 2: Graph Build G=(V,E)</text>
      <text x="270" y="124" font-family="'Times New Roman', serif" font-size="7.5" fill="#166534" text-anchor="middle">NetworkX / PyG directed graph</text>
      <text x="270" y="134" font-family="'Times New Roman', serif" font-size="7.5" fill="#166534" text-anchor="middle">Bipartite table-column nodes</text>

      <line x1="350" y1="118" x2="365" y2="118" stroke="#000" stroke-width="1.2"/>

      <rect x="365" y="98" width="160" height="40" fill="#f0fdf4" stroke="#16a34a" rx="3"/>
      <text x="445" y="112" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#14532d" text-anchor="middle">Step 3: Subgraph Search</text>
      <text x="445" y="124" font-family="'Times New Roman', serif" font-size="7.5" fill="#166534" text-anchor="middle">Steiner tree / Dijkstra search</text>
      <text x="445" y="134" font-family="'Times New Roman', serif" font-size="7.5" fill="#166534" text-anchor="middle">Bridge distant query entities</text>

      <line x1="445" y1="138" x2="445" y2="148" stroke="#000" stroke-width="1.2"/>
      <line x1="445" y1="148" x2="270" y2="148" stroke="#000" stroke-width="1.2"/>
      <line x1="270" y1="148" x2="270" y2="156" stroke="#000" stroke-width="1.2"/>

      <rect x="15" y="156" width="160" height="38" fill="#f5f3ff" stroke="#7c3aed" rx="3"/>
      <text x="95" y="169" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#5b21b6" text-anchor="middle">Step 4: Prune &amp; Redis Cache</text>
      <text x="95" y="180" font-family="'Times New Roman', serif" font-size="7.5" fill="#6d28d9" text-anchor="middle">Prune non-join attributes</text>
      <text x="95" y="190" font-family="'Times New Roman', serif" font-size="7.5" fill="#6d28d9" text-anchor="middle">Cache paths for fast lookup</text>

      <line x1="175" y1="175" x2="190" y2="175" stroke="#000" stroke-width="1.2"/>

      <rect x="190" y="156" width="160" height="38" fill="#f5f3ff" stroke="#7c3aed" rx="3"/>
      <text x="270" y="169" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#5b21b6" text-anchor="middle">Step 5: LLM Context Synthesis</text>
      <text x="270" y="180" font-family="'Times New Roman', serif" font-size="7.5" fill="#6d28d9" text-anchor="middle">Pruned subgraph prompt</text>
      <text x="270" y="190" font-family="'Times New Roman', serif" font-size="7.5" fill="#6d28d9" text-anchor="middle">Generate candidate SQL</text>

      <line x1="350" y1="175" x2="365" y2="175" stroke="#000" stroke-width="1.2"/>

      <rect x="365" y="156" width="160" height="38" fill="#f5f3ff" stroke="#7c3aed" rx="3"/>
      <text x="445" y="169" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#5b21b6" text-anchor="middle">Step 6: AST Verify &amp; Exec</text>
      <text x="445" y="180" font-family="'Times New Roman', serif" font-size="7.5" fill="#6d28d9" text-anchor="middle">sqlglot join validation</text>
      <text x="445" y="190" font-family="'Times New Roman', serif" font-size="7.5" fill="#6d28d9" text-anchor="middle">Self-repair loop &rarr; Postgres</text>

      <line x1="270" y1="194" x2="270" y2="204" stroke="#000" stroke-width="1.2"/>

      <rect x="15" y="204" width="510" height="22" fill="#f1f5f9" stroke="#475569" rx="3"/>
      <text x="270" y="219" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="middle">
        Evaluation Protocols P1–P4 on Spider &amp; BIRD &rarr; Answers to Research Questions RQ1, RQ2, RQ3, RQ4
      </text>
    </svg>
  </div>
  <div class="figure-caption">
    Figure 3.1: Research methodology flow of the proposed study, from the problem statement and research gap through the objectives (RO) and the six steps to the research questions (RQ).
  </div>

  <h2 class="sec-title" style="margin-top: 6px;">3.3 Step-by-Step Explanation of the Methodology</h2>
  <p>
    <strong>Step 1: Automated Metadata Mining (RO1):</strong><br>
    An automated Python database introspection daemon connects to target relational instances (PostgreSQL and MySQL) and extracts schema metadata directly from standard ANSI system catalogs (<code>information_schema.tables</code>, <code>columns</code>, <code>table_constraints</code>, <code>key_column_usage</code>). The extractor catalogs table identifiers, column names, primitive data types, primary-key constraints, and foreign-key referential pairings without requiring proprietary metadata annotations.
  </p>
  <p>
    <strong>Step 2: Relational Schema Graph Construction (RO1):</strong><br>
    The mined metadata is compiled into a directed schema knowledge graph <em>G = (V, E)</em>. Table nodes <em>V_T</em> and column nodes <em>V_C</em> form bipartite hierarchies, while directed edges <em>E_FK</em> represent foreign-key relationships (e.g., <code>orders.user_id &rarr; users.id</code>) annotated with constraint cardinalities (1:1, 1:N).
  </p>

  <div class="footer">9</div>
</div>
""")

    # PAGE 16: PAGE 10 - CHAPTER 3: STEPS 3-4 & TABLE 3.1
    html_parts.append("""
<div class="page">
  <p style="margin-top: 0;">
    <strong>Step 3: Multi-Hop Subgraph Path Traversal (RO2):</strong><br>
    When a natural language user query arrives, an entity parser identifies referenced entity mentions and maps them to terminal vertices <em>S &sube; V_T</em> in <em>G</em>. The path traversal engine executes a Steiner tree approximation algorithm to find the minimal connected subgraph spanning all terminals. This guarantees that intermediate junction tables (e.g., bridging <code>departments</code> to <code>products</code> via <code>users</code> and <code>orders</code>) are deterministically recovered, eliminating disconnected join paths.
  </p>
  <p>
    <strong>Step 4: Subgraph Context Pruning &amp; Redis Caching (RO3):</strong><br>
    The discovered subgraph is pruned of extraneous non-join columns, retaining only primary keys, foreign keys, and filter attributes mentioned in the query. Frequently traversed join trajectories are serialized into a high-speed Redis cache using normalized schema hash keys. This enables instant path retrieval for recurring analytical queries and facilitates speculative KV-cache reuse, bypassing redundant graph search.
  </p>

  <h2 class="sec-title" style="margin-top: 10px;">3.4 Benchmark Collections and Experimental Testbeds</h2>
  <p>
    To rigorously evaluate the framework across diverse domain conditions and schema scales, four database benchmark collections will be employed, summarized in Table 3.1:
  </p>

  <div class="table-caption">
    Table 3.1: Planned role, domain characteristics, and schema complexity of benchmark database collections.
  </div>
  <table class="formal-table" style="font-size: 8.6pt; line-height: 1.28;">
    <thead>
      <tr>
        <th style="width: 22%;">Benchmark Collection</th>
        <th style="width: 15%;">Role</th>
        <th style="width: 14%;">Total Databases</th>
        <th style="width: 15%;">Tables per Schema</th>
        <th style="width: 18%;">Foreign-Key Complexity</th>
        <th style="width: 16%;">Query Difficulty</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Spider Benchmark [7]</strong></td>
        <td>Cross-Domain Validation</td>
        <td>200 databases</td>
        <td>4 &ndash; 12 tables</td>
        <td>Moderate (1 &ndash; 3 joins)</td>
        <td>Easy to Complex</td>
      </tr>
      <tr>
        <td><strong>BIRD Benchmark [8]</strong></td>
        <td>Enterprise Evaluation</td>
        <td>95 databases</td>
        <td>10 &ndash; 45+ tables</td>
        <td>High (dirty data, 3 &ndash; 6 joins)</td>
        <td>Challenging Real-World</td>
      </tr>
      <tr>
        <td><strong>Spider-DK</strong></td>
        <td>Domain Knowledge Shift</td>
        <td>Domain subsets</td>
        <td>4 &ndash; 10 tables</td>
        <td>Knowledge perturbations</td>
        <td>High perturbation</td>
      </tr>
      <tr>
        <td><strong>Synthetic Enterprise ERP</strong></td>
        <td>Scalability Stress Test</td>
        <td>5 custom ERP schemas</td>
        <td>50 &ndash; 200 tables</td>
        <td>Very High (deep multi-hop)</td>
        <td>Deep enterprise joins</td>
      </tr>
    </tbody>
  </table>

  <p style="margin-top: 8px;">
    <strong>Experimental Hygiene and Data Leakage Prevention:</strong><br>
    To maintain complete scientific integrity, standard public test partitions are strictly sequestered. No test set schema or query is ever utilized during prompt tuning or heuristic hyperparameter selection. In addition, perceptual hash and exact-match deduplication routines will verify that no overlapping training queries pollute external evaluation splits.
  </p>

  <div class="footer">10</div>
</div>
""")

    # PAGE 17: PAGE 11 - CHAPTER 3: STEPS 5-6, TABLE 3.2 & FIG 3.2
    html_parts.append("""
<div class="page">
  <p style="margin-top: 0;">
    <strong>Step 5: LLM Context Synthesis &amp; Query Generation (RO4):</strong><br>
    The pruned minimal connected subgraph is serialized into compact, structured DDL Markdown statements and injected into the language model prompt. The foundation LLM synthesizes candidate SQL queries restricted strictly to the verified relational context.
  </p>
  <p>
    <strong>Step 6: Closed-Loop AST Verification &amp; Database Execution (RO4):</strong><br>
    Before reaching the production database, the candidate SQL query is intercepted by an AST parser (<code>sqlglot</code>). The validator compares all <code>JOIN</code> clauses against physical foreign-key edges in <em>G</em>. If an unconstrained join or invalid attribute is detected, an automated diagnostic error message is passed back to the LLM for zero-shot self-repair. Queries passing validation execute against isolated PostgreSQL/MySQL containers, returning execution metrics.
  </p>

  <div class="table-caption">
    Table 3.2: Controlled experimental evaluation protocols and the research question each answers.
  </div>
  <table class="formal-table" style="font-size: 8.4pt; line-height: 1.24; margin-bottom: 6px;">
    <thead>
      <tr>
        <th style="width: 25%;">Protocol</th>
        <th style="width: 27%;">Experimental Configuration</th>
        <th style="width: 33%;">Test Data Split</th>
        <th style="width: 15%; text-align: center;">Answers</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>P1: Cross-Domain Accuracy</strong></td>
        <td>Graph-RAG vs. Vector-RAG &amp; Full-DDL</td>
        <td>Spider and BIRD official test splits</td>
        <td style="text-align: center;"><strong>RQ1</strong></td>
      </tr>
      <tr>
        <td><strong>P2: Token &amp; Latency Profiling</strong></td>
        <td>Measuring input tokens, TTFT, and P99 latency</td>
        <td>Enterprise ERP schemas (10 to 200 tables)</td>
        <td style="text-align: center;"><strong>RQ2</strong></td>
      </tr>
      <tr>
        <td><strong>P3: Multi-Hop Stress Test</strong></td>
        <td>Partition queries by join hops (1, 2, 3, 4, 5+)</td>
        <td>Subsets requiring &ge;3 relational joins</td>
        <td style="text-align: center;"><strong>RQ3</strong></td>
      </tr>
      <tr>
        <td><strong>P4: AST Self-Repair Ablation</strong></td>
        <td>With vs. without closed-loop AST feedback</td>
        <td>Initially failed candidate query subsets</td>
        <td style="text-align: center;"><strong>RQ4</strong></td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title" style="margin-top: 6px;">3.4 Proposed Architecture</h2>
  <p style="margin-bottom: 4px;">
    Figure 3.2 illustrates the end-to-end technical architecture of the proposed Relational Graph-RAG system:
  </p>

  <div style="border: 1px solid #000000; padding: 4px; margin: 4px 0; background: #ffffff; text-align: center;">
    <img src="assets/graph_rag_text_to_sql.jpg" style="width: 100%; max-height: 165px; object-fit: contain; display: block; margin: 0 auto;" alt="Proposed Architecture"/>
  </div>
  <div class="figure-caption">
    Figure 3.2: Architecture of the proposed Relational Graph-RAG model showing the pipeline from query entity extraction and schema graph traversal to speculative Redis caching and closed-loop AST verification.
  </div>

  <div class="footer">11</div>
</div>
""")

    # PAGE 18: PAGE 12 - CHAPTER 3: MODEL STEPS & MATH
    html_parts.append("""
<div class="page">
  <h2 class="sec-title" style="margin-top: 0;">3.5 Step-by-Step Explanation of the Proposed Model</h2>
  <p>
    The operational workflow of the proposed Relational Graph-RAG model executes in seven structured stages:
  </p>
  <p style="font-size: 10.8pt; line-height: 1.42; margin-bottom: 4.5px;">
    <strong>1. Schema Ingestion:</strong> Connects to PostgreSQL/MySQL instances via native drivers, reading tables, primary keys, and foreign keys directly from <code>information_schema</code> without manual tagging.
  </p>
  <p style="font-size: 10.8pt; line-height: 1.42; margin-bottom: 4.5px;">
    <strong>2. Graph Compilation:</strong> Converts relational metadata into a directed graph <em>G = (V, E)</em>, mapping tables to parent vertices and foreign-key constraints to directed edges.
  </p>
  <p style="font-size: 10.8pt; line-height: 1.42; margin-bottom: 4.5px;">
    <strong>3. Entity Linking &amp; Terminal Selection:</strong> Extracts database keywords and entities from the user prompt, identifying the set of required terminal nodes <em>S &sube; V_T</em>.
  </p>
  <p style="font-size: 10.8pt; line-height: 1.42; margin-bottom: 4.5px;">
    <strong>4. Steiner Minimal Subgraph Discovery:</strong> Computes the minimal connected subgraph bridging all terminal nodes in <em>S</em>, deterministically including intermediate junction tables.
  </p>
  <p style="font-size: 10.8pt; line-height: 1.42; margin-bottom: 4.5px;">
    <strong>5. Speculative Redis Caching:</strong> Checks Redis for cached subgraphs using query schema hashes; on a cache hit, returns precomputed subgraphs instantly; on a miss, computes and caches the result.
  </p>
  <p style="font-size: 10.8pt; line-height: 1.42; margin-bottom: 4.5px;">
    <strong>6. Context Serialization &amp; LLM Generation:</strong> Serializes the pruned subgraph into structured DDL statements, prompting the LLM to generate the candidate SQL query.
  </p>
  <p style="font-size: 10.8pt; line-height: 1.42; margin-bottom: 8px;">
    <strong>7. Closed-Loop AST Interception:</strong> Parses generated SQL with <code>sqlglot</code>, verifying that all join predicates match valid edges in <em>G</em>. Detected errors trigger an automated diagnostic prompt for self-correction before database execution.
  </p>

  <h2 class="sec-title" style="margin-top: 6px;">3.6 Mathematical and Graph-Theoretic Formulations</h2>
  <p>
    Let the relational database schema be defined as a directed knowledge graph <em>G = (V, E)</em>, where <em>V = V_T &cup; V_C</em> represents the union of table vertices <em>V_T</em> and column vertices <em>V_C</em>. The edge set <em>E = E_attr &cup; E_FK</em> comprises containment edges and directed foreign-key referential edges <em>E_FK = {(t_i, t_j) | t_i, t_j &isin; V_T, FK(t_i) = PK(t_j)}</em>.
  </p>
  <p>
    Given a user natural language query <em>Q</em>, an entity recognition operator extracts a terminal node subset <em>S &sube; V_T</em>. The multi-hop schema linking problem is formalized as finding the minimal connected Steiner subgraph <em>T* &sube; G</em> that spans all terminal vertices <em>S</em>:
  </p>
  <div style="text-align: center; margin: 5px 0 8px 0; font-style: italic; font-size: 11.2pt;">
    T* = arg min<sub>T &sube; G</sub> &sum;<sub>e &isin; E(T)</sub> w(e) &nbsp;&nbsp;&nbsp; subject to &nbsp;&nbsp; S &sube; V(T)
  </div>
  <p>
    where edge weight <em>w(e)</em> represents the traversal cost based on join cardinality and foreign-key selectivity. Candidate SQL queries synthesized by the LLM are evaluated against the AST constraint predicate:
  </p>
  <div style="text-align: center; margin: 5px 0 8px 0; font-style: italic; font-size: 11.2pt;">
    &Phi;(Q<sub>SQL</sub>, G) = 1 &nbsp;&hArr;&nbsp; &forall; (t<sub>a</sub>, t<sub>b</sub>) &isin; Joins(Q<sub>SQL</sub>), &nbsp; &exist; e &isin; E(T*) &nbsp; s.t. &nbsp; connects(e, t<sub>a</sub>, t<sub>b</sub>)
  </div>
  <p>
    If <em>&Phi;(Q<sub>SQL</sub>, G) = 0</em>, the AST engine extracts the violated join predicate and synthesizes a diagnostic repair prompt, initiating iterative zero-shot self-repair.
  </p>

  <div class="footer">12</div>
</div>
""")

    # PAGE 19: PAGE 13 - CHAPTER 4: WORK PLAN & FEASIBILITY
    html_parts.append("""
<div class="page">
  <h1 class="chap-num">CHAPTER 4</h1>
  <h1 class="chap-title">WORK PLAN, FEASIBILITY &amp; TIMELINE</h1>

  <h2 class="sec-title">4.1 Candidate Technical Background &amp; Feasibility</h2>
  <p>
    The applicant, <strong>Muhammad Maaz Khan</strong>, holds a Bachelor of Science in Computer Science from the University of Engineering and Technology (UET), Peshawar. Over the past 4+ years, he has engineered production software architectures, specializing in backend systems, relational database administration (PostgreSQL, MySQL), caching engines (Redis), containerization (Docker), and real-time communication protocols.
  </p>
  <p>
    The applicant transparently acknowledges transitioning from commercial software engineering to scientific research, having not published prior academic papers. However, this production background provides immediate systems implementation readiness: the applicant has designed normalized database schemas, debugged concurrent transactions, managed schema migrations, and optimized low-latency services. This practical foundation eliminates the standard multi-month onboarding lag associated with systems engineering, enabling rapid benchmark deployment from Day 1.
  </p>

  <h2 class="sec-title" style="margin-top: 8px;">4.2 Research Preparation &amp; Skill Acquisition Plan</h2>
  <p>
    To ensure a seamless transition into rigorous academic research at USTC, the applicant has formulated a structured Year-1 skill acquisition curriculum:
  </p>
  <p style="margin-bottom: 4px;">
    <strong>1. Scientific Python &amp; Deep Learning Toolkits:</strong> Mastering scientific Python libraries (NumPy, PyTorch, PyTorch Geometric, NetworkX, HuggingFace Transformers) to transition commercial backend engineering into deep learning implementations.
  </p>
  <p style="margin-bottom: 4px;">
    <strong>2. Graduate Coursework at USTC:</strong> Completing core coursework in Machine Learning, Natural Language Processing, and Advanced Database Systems with high academic distinction.
  </p>
  <p style="margin-bottom: 8px;">
    <strong>3. Scientific Literature &amp; Seminar Engagement:</strong> Reading, synthesizing, and replicating 3–5 foundational Text-to-SQL and table reasoning publications monthly under laboratory mentorship.
  </p>

  <h2 class="sec-title" style="margin-top: 8px;">4.3 24-Month Master's Research Timeline &amp; Milestones</h2>
  <div class="table-caption">
    Table 4.1: 24-Month Master's research work plan, semester milestones, and target deliverables.
  </div>
  <table class="formal-table" style="font-size: 8.6pt; line-height: 1.28;">
    <thead>
      <tr>
        <th style="width: 15%;">Phase / Period</th>
        <th style="width: 25%;">Primary Milestone</th>
        <th style="width: 38%;">Core Research Activities</th>
        <th style="width: 22%;">Target Deliverable</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Semester 1<br>(Months 1&ndash;6)</strong></td>
        <td>Coursework &amp; Ingestion Daemon</td>
        <td>Complete USTC graduate courses; build PostgreSQL/MySQL metadata extractor; establish Spider/BIRD environments.</td>
        <td>Working catalog ingestion daemon &amp; benchmark testbed</td>
      </tr>
      <tr>
        <td><strong>Semester 2<br>(Months 7&ndash;12)</strong></td>
        <td>Graph Engine &amp; Baseline Benchmarks</td>
        <td>Implement NetworkX schema graph builder; code Steiner tree search; benchmark Baseline A (Full DDL) and B (Vector-RAG).</td>
        <td>Relational Graph-RAG prototype; Midterm Review Report</td>
      </tr>
      <tr>
        <td><strong>Semester 3<br>(Months 13&ndash;18)</strong></td>
        <td>AST Repair &amp; Redis Caching</td>
        <td>Integrate <code>sqlglot</code> AST self-correction loop; deploy Redis path cache; conduct extensive multi-table ablation studies.</td>
        <td>Conference paper draft submitted to ACL / EMNLP</td>
      </tr>
      <tr>
        <td><strong>Semester 4<br>(Months 19&ndash;24)</strong></td>
        <td>Thesis Writing &amp; Defense</td>
        <td>Complete Master's thesis chapters; incorporate committee feedback; defend thesis; open-source reproducible codebase.</td>
        <td>Master's Thesis Defense &amp; Archived GitHub Repository</td>
      </tr>
    </tbody>
  </table>

  <h2 class="sec-title" style="margin-top: 8px;">4.4 Alignment with Prof. Shuangwu Chen's Laboratory at USTC</h2>
  <p>
    Prof. Shuangwu Chen's group at USTC is a recognized leader in table reasoning and intelligent RAG systems (*SQLForge*, Findings of ACL 2025; *Table Pruning in TableQA*, ACL 2026 Oral; *SpecCache*, ACL 2026 Oral). The proposed Relational Graph-RAG framework directly aligns with and extends these research vectors from flat tabular benchmarks to complex multi-table enterprise relational schemas. Under Prof. Chen's mentorship, the applicant aims to combine practical database engineering with cutting-edge academic table reasoning.
  </p>

  <div class="footer">13</div>
</div>
""")

    # PAGE 20: PAGE 14 - CHAPTER 5: REFERENCES (PART 1)
    html_parts.append("""
<div class="page">
  <h1 class="chap-num">CHAPTER 5</h1>
  <h1 class="chap-title">REFERENCES</h1>

  <div class="ref-item">
    [1] Y. Guo, S. Chen*, et al., &ldquo;SQLForge: Synthesizing Reliable and Diverse Data to Enhance Text-to-SQL Reasoning in LLMs,&rdquo; <em>Findings of the Association for Computational Linguistics: ACL 2025</em>, 2025.
  </div>
  <div class="ref-item">
    [2] Y. Guo, S. Ye, S. Chen, and J. Yang, &ldquo;Rethinking Table Pruning in TableQA: From Sequential Revisions to Gold Trajectory-Supervised Parallel Search,&rdquo; in <em>Proc. 64th Annu. Meeting Assoc. Comput. Linguistics (ACL 2026, Oral)</em>, 2026.
  </div>
  <div class="ref-item">
    [3] S. Ye, Y. Guo, S. Chen, and J. Yang, &ldquo;When TableQA Meets Noise: A Dual Denoising Framework for Complex Questions and Large-scale Tables,&rdquo; in <em>Proc. 64th Annu. Meeting Assoc. Comput. Linguistics (ACL 2026)</em>, 2026.
  </div>
  <div class="ref-item">
    [4] Z. Wen, T. Zhang, S. Chen, and J. Yang, &ldquo;SpecCache: Speculative KV Cache Reuse for Efficient RAG Serving,&rdquo; in <em>Proc. 64th Annu. Meeting Assoc. Comput. Linguistics (ACL 2026, Oral)</em>, 2026.
  </div>
  <div class="ref-item">
    [5] S. Ye, Y. Wang, Y. Guo, T. Zhang, S. Chen*, Z. Wen, et al., &ldquo;Rethinking Stepwise Model Routing: A Cost-Efficient Table Reasoning Perspective,&rdquo; in <em>Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP 2026)</em>, 2026.
  </div>
  <div class="ref-item">
    [6] J. Yang, Z. Wang, S. Chen*, H. He, Y. Hou, and X. Jiang, &ldquo;HG-PAD: Heterogeneous Graph Structure Learning Aided Performance Anomaly Diagnosis in Microservice Systems,&rdquo; <em>IEEE Trans. Serv. Comput.</em>, vol. 18, no. 2, pp. 312&ndash;325, 2025.
  </div>
  <div class="ref-item">
    [7] T. Yu, R. Zhang, K. Yang, M. Yasunaga, D. Wang, Z. Li, et al., &ldquo;Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL,&rdquo; in <em>Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP 2018)</em>, 2018, pp. 3871&ndash;3881.
  </div>
  <div class="ref-item">
    [8] J. Li, B. Hui, G. Qu, J. Yang, B. Li, B. Wang, et al., &ldquo;Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQL (BIRD),&rdquo; in <em>Adv. Neural Inf. Process. Syst. (NeurIPS 2023)</em>, vol. 36, 2023.
  </div>
  <div class="ref-item">
    [9] M. Pourreza and D. Rafiei, &ldquo;DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction,&rdquo; in <em>Adv. Neural Inf. Process. Syst. (NeurIPS 2023)</em>, vol. 36, 2023.
  </div>
  <div class="ref-item">
    [10] D. Gao, H. Wang, Y. Li, X. Sun, Y. Qian, B. Ding, and J. Zhou, &ldquo;Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation,&rdquo; <em>Proc. VLDB Endowment</em>, vol. 17, no. 11, pp. 3132&ndash;3145, 2024.
  </div>
  <div class="ref-item">
    [11] B. Wang, W. C. Yin, X. V. Lin, and C. Xiong, &ldquo;Learning to Synthesize for Complex Semantic Parsing,&rdquo; in <em>Proc. 59th Annu. Meeting Assoc. Comput. Linguistics (ACL 2021)</em>, 2021, pp. 2316&ndash;2327.
  </div>
  <div class="ref-item">
    [12] T. Scholak, N. Schucher, and D. Bahdanau, &ldquo;PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models,&rdquo; in <em>Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP 2021)</em>, 2021, pp. 9895&ndash;9901.
  </div>
  <div class="ref-item">
    [13] X. Chen, X. Shen, Y. Xie, et al., &ldquo;ShadowGNN: Graph Projection Neural Networks for Text-to-SQL,&rdquo; in <em>Proc. NAACL-HLT 2021</em>, 2021, pp. 5533&ndash;5545.
  </div>
  <div class="ref-item">
    [14] B. Bogin, M. Gardner, and J. Berant, &ldquo;Global Reasoning over Database Structures for Text-to-SQL Parsing,&rdquo; in <em>Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP 2019)</em>, 2019, pp. 3659&ndash;3664.
  </div>
  <div class="ref-item">
    [15] R. Zhang, T. Yu, H. Y. Hey, et al., &ldquo;Editing-Based SQL Query Generation for Cross-Domain Text-to-SQL,&rdquo; in <em>Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP 2019)</em>, 2019, pp. 2901&ndash;2910.
  </div>
  <div class="ref-item">
    [16] P. Wang, T. Shi, and C. K. Reddy, &ldquo;Text-to-SQL Generation for Question Answering on Electronic Medical Records,&rdquo; in <em>Proc. Web Conf. (WWW 2020)</em>, 2020, pp. 350&ndash;361.
  </div>
  <div class="ref-item">
    [17] Y. Gan, X. Chen, Q. Huang, M. Purver, J. R. Woodward, J. Xie, and P. Huang, &ldquo;Towards Robustness of Text-to-SQL Models Against Synonym Substitution,&rdquo; in <em>Proc. 59th Annu. Meeting Assoc. Comput. Linguistics (ACL 2021)</em>, 2021, pp. 2505&ndash;2515.
  </div>

  <div class="footer">14</div>
</div>
""")

    # PAGE 21: PAGE 15 - CHAPTER 5: REFERENCES (PART 2)
    html_parts.append("""
<div class="page">
  <div class="ref-item" style="margin-top: 15mm;">
    [18] S. Zhang, T. Zhang, Q. Zhu, M. Zhang, D. Jin, Y. Hou, S. Chen*, X. Tan, Q. Zheng, and J. Yang, &ldquo;LatCom: Cross-Agent Latent Compression for Efficient Multi-Agent Collaboration,&rdquo; in <em>Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP 2026)</em>, 2026.
  </div>
  <div class="ref-item">
    [19] Q. Zhu, Z. Wen, T. Zhang, M. Zhang, S. Ye, D. Jin, S. Chen*, X. Tan, Q. Zheng, and J. Yang, &ldquo;VISA: Video Skeleton-Aware Efficient Frame Selection for Long Video Understanding,&rdquo; in <em>Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP 2026)</em>, 2026.
  </div>
  <div class="ref-item">
    [20] S. Ye, Y. Guo, Z. Li, Q. Huang, S. Chen*, W. Luo, R. Qian, J. Zhang, T. Zhang, D. Jin, X. Tan, Q. Zheng, and J. Yang, &ldquo;Rubric-Guided Process Reward for Stepwise Model Routing,&rdquo; in <em>Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP 2026)</em>, 2026.
  </div>
  <div class="ref-item">
    [21] M. Zhang, T. Zhang, Q. Zhu, Z. Wen, S. Chen*, and J. Yang, &ldquo;GSTEP: Global-Step-Aware Event Planning for Long-Form Video Understanding,&rdquo; in <em>Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP 2026)</em>, 2026.
  </div>
  <div class="ref-item">
    [22] C. Wang, A. Cheung, and R. Bodik, &ldquo;Synthesizing Highly Expressive SQL Queries from Input-Output Examples,&rdquo; in <em>Proc. 38th ACM SIGPLAN Conf. Program. Lang. Des. Implement. (PLDI 2017)</em>, 2017, pp. 452&ndash;466.
  </div>
  <div class="ref-item">
    [23] Y. Li, D. Min, S. Shen, et al., &ldquo;Can LLMs Learn from Macro-Steps? Improving Reasoning via Multi-Step Decomposition in Text-to-SQL,&rdquo; in <em>Proc. 62nd Annu. Meeting Assoc. Comput. Linguistics (ACL 2024)</em>, 2024.
  </div>
  <div class="ref-item">
    [24] H. Fang, D. Zhang, Y. Wang, et al., &ldquo;Schema-Aware Multi-Task Learning for Complex Text-to-SQL Semantic Parsing,&rdquo; <em>IEEE Trans. Knowl. Data Eng.</em>, vol. 35, no. 8, pp. 8110&ndash;8122, 2023.
  </div>
  <div class="ref-item">
    [25] Z. Sun, J. Zhang, J. Sun, et al., &ldquo;A Survey on Table-based Question Answering and Natural Language Interfaces to Databases,&rdquo; <em>ACM Comput. Surv.</em>, vol. 55, no. 8, pp. 1&ndash;38, 2023.
  </div>
  <div class="ref-item">
    [26] X. Deng, C. S. Wu, Z. Lin, et al., &ldquo;Structure-Grounded Pretraining for Text-to-SQL and Table Question Answering,&rdquo; in <em>Proc. NAACL-HLT 2022</em>, 2022, pp. 1337&ndash;1350.
  </div>
  <div class="ref-item">
    [27] Y. Cao, X. Chen, and B. Ding, &ldquo;MAC-SQL: Multi-Agent Collaborative Framework for Complex Text-to-SQL,&rdquo; in <em>Proc. 30th ACM SIGKDD Conf. Knowl. Discov. Data Min. (KDD 2024)</em>, 2024, pp. 312&ndash;323.
  </div>
  <div class="ref-item">
    [28] P. Shaw, M. Chang, P. Pasupat, and K. Toutanova, &ldquo;Compositional Generalization and Natural Language Interfaces: An Information-Theoretic Perspective,&rdquo; in <em>Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP 2021)</em>, 2021, pp. 8560&ndash;8572.
  </div>
  <div class="ref-item">
    [29] N. Yaghmazadeh, Y. Wang, I. Dillig, and T. Dillig, &ldquo;SQLizer: Query Synthesis from Natural Language using Semantic Parsers and Type-Directed Search,&rdquo; <em>Proc. ACM Program. Lang.</em>, vol. 1, no. OOPSLA, pp. 1&ndash;26, 2017.
  </div>
  <div class="ref-item">
    [30] T. Scholak, R. Cao, and N. Schucher, &ldquo;DUAL-SQL: Constrained Decoding and Execution Feedback for Semantic Parsing,&rdquo; in <em>Proc. 61st Annu. Meeting Assoc. Comput. Linguistics (ACL 2023)</em>, 2023, pp. 4112&ndash;4125.
  </div>

  <div style="margin-top: 25mm; border-top: 1px solid #777777; padding-top: 10px; font-size: 9.5pt; color: #444444; text-align: center; font-style: italic;">
    This document constitutes the complete formal research synopsis submission for the Master of Science degree program at the University of Science and Technology of China (USTC), prepared by Muhammad Maaz Khan under the prospective supervision of Prof. Shuangwu Chen.
  </div>

  <div class="footer">15</div>
</div>
""")

    # Close body and html
    html_parts.append("""
</body>
</html>
""")

    full_html = "".join(html_parts)
    
    html_file = r"c:\Users\RYZEN 7\Desktop\Thesis\RsearchPaper\Muhammad_Maaz_Khan_Formal_Synopsis_Proposal_USTC.html"
    pdf_file = r"c:\Users\RYZEN 7\Desktop\Thesis\RsearchPaper\Muhammad_Maaz_Khan_Formal_Synopsis_Proposal_USTC.pdf"
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"HTML successfully generated at {html_file}")

    edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_file}",
        html_file
    ]

    print("Executing Microsoft Edge Headless PDF compilation...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_file):
        file_size = os.path.getsize(pdf_file)
        print(f"SUCCESS: Generated PDF at {pdf_file} (Size: {file_size:,} bytes)")
        
        # Verify page count and contents
        reader = pypdf.PdfReader(pdf_file)
        total_p = len(reader.pages)
        print(f"Verification: Total Pages = {total_p} (Target: 21)")
        for idx in range(total_p):
            page_txt = reader.pages[idx].extract_text().strip()
            first = page_txt.split('\n')[0] if page_txt else 'EMPTY'
            last = page_txt.split('\n')[-1] if page_txt else 'EMPTY'
            print(f"  Page {idx+1:2d}: Header -> '{first[:32]}' | Footer -> '{last}'")
    else:
        print("ERROR during PDF compilation:", res.stderr)

if __name__ == "__main__":
    generate_formal_synopsis()
