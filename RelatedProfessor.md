Ran command: `python -c "
import zipfile, xml.etree.ElementTree as ET

docx_path = r'c:\Users\RYZEN 7\Desktop\Thesis\RsearchPaper\IDEA1\ResearchPaperTeacherForScholarship.docx'
with zipfile.ZipFile(docx_path) as z:
    xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    text = []
    for node in tree.iter():
        if node.tag.endswith('t'):
            text.append(node.text or '')
    print(''.join(text))
"`
Ran command: `python -c "
import zipfile, xml.etree.ElementTree as ET, sys
sys.stdout.reconfigure(encoding='utf-8')

docx_path = r'c:\Users\RYZEN 7\Desktop\Thesis\RsearchPaper\IDEA1\ResearchPaperTeacherForScholarship.docx'
with zipfile.ZipFile(docx_path) as z:
    xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    
    # Let's inspect paragraphs and tables
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    body = tree.find('w:body', namespaces)
    if body is not None:
        for p in body.findall('w:p', namespaces):
            texts = [t.text for t in p.iter() if t.tag.endswith('t') and t.text]
            line = ''.join(texts).strip()
            if line:
                print('P:', line)
        for tbl in body.findall('w:tbl', namespaces):
            print('--- TABLE ---')
            for tr in tbl.findall('w:tr', namespaces):
                row = []
                for tc in tr.findall('w:tc', namespaces):
                    tc_text = ''.join([t.text for t in tc.iter() if t.tag.endswith('t') and t.text]).strip()
                    row.append(tc_text)
                print(' | '.join(row))
"`
Searched web: "USTC "medical image" OR "medical imaging" professor computer science OR information science"
Searched web: ""S. Kevin Zhou" USTC email OR "MIRACLE" lab USTC"
Searched web: "UCAS OR "Institute of Automation" "medical image" OR "medical imaging" professor OR "CASIA""
Searched web: "SIAT "medical image" OR "medical imaging" professor CAS UCAS"
Searched web: ""Wengang Zhou" USTC "medical" OR "computer vision""
Searched web: "ICT CAS OR "Institute of Computing Technology" "medical image" professor"
Searched web: ""Hu Han" "ICT" CAS email OR "vipl.ict.ac.cn""
Searched web: ""Shuhui Wang" "ICT" CAS email OR "wangshuhui""
Searched web: ""Shanshan Wang" "SIAT" email ucas.ac.cn OR siat.ac.cn"
Searched web: "USTC "domain generalization" OR "out-of-distribution" professor"
Searched web: ""Beier Zhu" USTC email"
Searched web: "CASIA OR "Institute of Automation" "medical image" deep learning professor email"
Searched web: ""Jie Tian" CASIA OR UCAS medical image email"

Based on an analysis of your proposal **DermFusion-DG** (*Multimodal Fusion, Missing Modality Handling, Domain Generalisation, and Skin Cancer Classification*) and the document [ResearchPaperTeacherForScholarship.docx](file:///c:/Users/RYZEN%207/Desktop/Thesis/RsearchPaper/IDEA1/ResearchPaperTeacherForScholarship.docx), here is the detailed evaluation:

---

### Part 1: Review of the Professors Already in Your List

Your Word document only looked at the general **School of Computer Science**. Most of them work on hardware, cloud networking, or cryptography (which are **not** relevant to your medical AI proposal). 

Here are the only ones from your existing list that are relevant:

| Professor & Affiliation | Research Field | Relevance to Your Proposal | Recommendation |
| :--- | :--- | :--- | :--- |
| **Chang Xiaojun (常晓军)**<br>USTC — `xjchang@ustc.edu.cn` | Multimodal Large Models, Computer Vision | **High (8.5/10)**: Strong in multimodal learning and vision transformers. | **Email him!** (Top pick from your existing USTC list). |
| **Ma Bingpeng (马丙鹏)**<br>UCAS — `bpma@ucas.ac.cn` | Computer Vision, Metric Learning, Domain Adaptation | **Medium-High (7.5/10)**: Excellent in domain adaptation & feature representation. | **Email him!** (Good pick from your existing UCAS list). |
| **Su Li (苏荔)**<br>UCAS — `suli@ucas.ac.cn` | Multimedia, Image Processing, CV | **Medium (6.5/10)**: Works on multimedia image analysis. | Backup option. |
| **Huanhuan Chen**<br>USTC — `hchen@ustc.edu.cn` | Machine Learning, Data Mining | **Medium (6.0/10)**: General ML methods, less medical-specific. | Backup option. |
| **All others in your doc** *(e.g., networking, chip design, cryptography)* | Hardware, Networks, Systems | **Irrelevant (1/10)** | **Do NOT email** for this proposal. |

---

### Part 2: The "Missing Champions" at USTC & UCAS Found Online

Because your proposal is at the intersection of **Medical Image Computing (MICCAI)**, **Multimodal AI**, and **Domain Generalisation**, the top supervisors in China are located in specialized Medical AI Labs and CAS Institutes affiliated with USTC and UCAS (such as the **MIRACLE Lab**, **SIAT**, **CASIA**, and **ICT VIPL Lab**). 

Here are the professors that were **missing from your list**:

---

#### 🏫 1. At USTC (University of Science and Technology of China)

#### 🥇 **Prof. S. Kevin Zhou (周少华)** — *The Absolute #1 Best Match in China*
* **Title:** Executive Dean, School of Biomedical Engineering; Director, Center for Medical Imaging, Robotics, Analytic Computing and Learning (**MIRACLE Lab**), USTC.
* **Email:** `skevinzhou@ustc.edu.cn`
* **Profile:** Past President of the **MICCAI Society** (the top world conference for medical imaging), IEEE Fellow, AIMBE Fellow.
* **Why He Matches DermFusion-DG:** His entire lab focuses on **medical image computing, multimodal deep learning in healthcare, label-efficient learning, and domain adaptation**. Your proposal reads like a project from his lab.
* **Verdict:** **Top Priority #1 for USTC.**

#### 🥈 **Prof. Beier Zhu (朱贝尔)** — *Domain Generalisation & Robust AI Expert*
* **Title:** Professor, School of Computer Science / Big Data, USTC.
* **Email:** `beier.zhu@ustc.edu.cn`
* **Why He Matches DermFusion-DG:** His primary research focus is **Out-of-Distribution (OOD) Generalization, Domain Generalization (DG), and Foundation Model Robustness**. If you want a supervisor who is an expert in the math and techniques of the "DG" part of your thesis, he is an exact match.
* **Verdict:** **Top Priority #2 for USTC.**

---

#### 🏫 2. At UCAS / Chinese Academy of Sciences (CAS) Institutes
*(Note: As an ANSO applicant to UCAS, you can apply directly under supervisors at CAS Institutes—these institutes award UCAS degrees!)*

#### 🥇 **Prof. Shanshan Wang (王珊珊)** — *UCAS / SIAT (Shenzhen Institute of Advanced Technology)*
* **Title:** Full Professor & Doctoral Supervisor, Paul C. Lauterbur Research Center / Institute of Biomedical and Health Engineering, SIAT CAS.
* **Email:** `ss.wang@siat.ac.cn`
* **Profile:** Associate Editor of **IEEE Transactions on Medical Imaging (TMI)**.
* **Why She Matches DermFusion-DG:** Specializes in **Medical AI, Multimodal Medical Analysis, Radiomics, and Deep Learning for clinical diagnostics**. SIAT has the largest medical imaging computing center in the Chinese Academy of Sciences.
* **Verdict:** **Top Priority #1 for UCAS.**

#### 🥈 **Prof. Hu Han (韩琥)** — *UCAS / ICT (Institute of Computing Technology, CAS)*
* **Title:** Professor, Visual Intelligence for Robots, Agents, and Foundation Models (**VIPL Group**), ICT CAS.
* **Email:** `hanhu@ict.ac.cn` or `hu.han@vipl.ict.ac.cn`
* **Why He Matches DermFusion-DG:** Highly active in **medical image analysis, computer vision, domain-invariant representation, and cross-modality feature learning**.
* **Verdict:** **Top Priority #2 for UCAS.**

#### 🥉 **Prof. Shuhui Wang (王树徽)** — *UCAS / ICT (Institute of Computing Technology, CAS)*
* **Title:** Professor, VIPL Group, ICT CAS.
* **Email:** `wangshuhui@ict.ac.cn`
* **Why He Matches DermFusion-DG:** Internationally recognized in **multimodal representation learning, cross-modal attention, and medical image segmentation**. Directly fits your cross-modal transformer fusion.
* **Verdict:** **High Priority for UCAS.**

#### 🏅 **Prof. Jie Tian (田捷)** & **Dr. Di Dong (董迪)** — *UCAS / CASIA (Institute of Automation, CAS)*
* **Title:** Molecular Imaging & Radiomics Lab, CASIA.
* **Emails:** `jie.tian@ia.ac.cn`, `di.dong@ia.ac.cn`
* **Why They Match DermFusion-DG:** Pioneers of medical AI in CASIA, focusing on **cancer detection, tumor radiomics, and multi-source medical big data**.
* **Verdict:** **Strong Priority for UCAS.**

---

### Part 3: Ranked Priority Email List for ANSO Scholarship

When applying for the ANSO Scholarship, you should email supervisors in this prioritized order:

| Rank | Professor | University / Institute | Email | Specific Pitch Angle |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **S. Kevin Zhou** | USTC (MIRACLE Lab) | `skevinzhou@ustc.edu.cn` | Pitch: Multimodal medical image analysis + clinical dermatology foundation models. |
| **2** | **Shanshan Wang** | UCAS / SIAT | `ss.wang@siat.ac.cn` | Pitch: Multimodal clinical fusion + robust cancer classification. |
| **3** | **Beier Zhu** | USTC (CS & Data) | `beier.zhu@ustc.edu.cn` | Pitch: Out-of-distribution (OOD) & domain generalization for medical models. |
| **4** | **Hu Han** | UCAS / ICT (VIPL) | `hanhu@ict.ac.cn` | Pitch: Medical computer vision + incomplete modality handling. |
| **5** | **Xiaojun Chang** | USTC (CS) | `xjchang@ustc.edu.cn` | Pitch: Multimodal foundation models + vision-language fusion. |
| **6** | **Shuhui Wang** | UCAS / ICT | `wangshuhui@ict.ac.cn` | Pitch: Cross-modal transformer fusion for healthcare. |
| **7** | **Bingpeng Ma** | UCAS (CS) | `bpma@ucas.ac.cn` | Pitch: Feature domain adaptation & representation learning. |

---

### Part 4: How to Personalize Your Email (Key Talking Points)

To maximize your chances of getting a fast acceptance letter from these professors:

1. **Subject Line Formula:**
   > `ANSO Scholarship Application 2026 - PhD Candidate - Prospective Student [Your Name] (Research Proposal: DermFusion-DG)`

2. **Mentioning the Match:**
   * When writing to **Prof. S. Kevin Zhou** or **Prof. Shanshan Wang**, highlight: *"My proposal, DermFusion-DG, addresses missing modalities and domain shift in dermatology image computing, directly aligning with your lab’s work on multimodal medical AI and MICCAI-standard benchmarks."*
   * When writing to **Prof. Beier Zhu**, highlight: *"My proposed framework focuses on resolving domain shift via MixStyle, CORAL, and domain-adversarial learning to ensure OOD robustness across clinical domains."*
3. **Attach:**
   * Your CV.
   * The **[DermFusion_DG_Proposal_Simple_Guide.pdf](file:///c:/Users/RYZEN%207/Desktop/Thesis/RsearchPaper/IDEA1/DermFusion_DG_Proposal_Simple_Guide.pdf)** or your formal proposal summary so they can see your research methodology immediately.
