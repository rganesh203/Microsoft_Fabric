# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# # Microsoft Fabric hierarchy
#  Microsoft Fabric hierarchy in complete detail: Tenant → Capacity → Workspace → Items — with examples, diagrams (conceptually), and use cases where applicable.

# MARKDOWN ********************

# # 🌐 1. Tenant
# 
# ### 🧩 What is a Tenant?
# 
# A tenant in Microsoft Fabric is the top-level container that represents your organization in the Microsoft Cloud (typically tied to your Azure Active Directory domain, like yourcompany.com).
# 
# Think of it as your entire organization’s environment.
# 
# ### 🔐 Characteristics:
# 
# Unique to an organization (like ganesh@contoso.com is part of contoso.com tenant).
# 
# Manages users, roles, permissions, data governance, and compliance policies.
# 
# Can have multiple capacities and many workspaces.
# 
# ### ✅ Example:
# 
# Contoso Ltd has a Microsoft 365 tenant with domain contoso.com.
# 
# This tenant will host Microsoft Fabric resources (like dataflows, pipelines, reports) used across departments like Finance, HR, and Sales.

# MARKDOWN ********************

# # ⚙️ 2. Capacity
# 
# ### 🧩 What is Capacity?
# A capacity is a set of dedicated resources (CPU, RAM, Storage) that powers the operations within Fabric — such as running pipelines, storing data, and processing queries.
# 
# Think of it as a server or resource pool.
# 
# ### 📊 Types of Capacity:
# Trial Capacity: Limited, free, used for testing.
# 
# Pro Capacity: Shared capacity (for small orgs or individuals).
# 
# Fabric Capacity (F SKUs): Dedicated and scalable (e.g., F2, F4, F8) with more power for enterprise workloads.
# 
# ### 🔐 Characteristics:
# Tied to a region (e.g., India Central).
# 
# Can be shared across multiple workspaces.
# 
# Needed to enable full Fabric functionality (e.g., dataflows, Spark notebooks).
# 
# ### ✅ Example:
# Contoso purchases F4 Capacity in the India Central region to support large-scale data processing for analytics projects.

# MARKDOWN ********************

# # 🗃️ 3. Workspace
# 
# ### 🧩 What is a Workspace?
# A workspace is a collaborative container for organizing and managing Fabric items (like data, reports, pipelines) for a team or project.
# 
# Think of it like a folder/project for your department.
# 
# ### 🔐 Characteristics:
# Connected to one capacity.
# 
# Can be assigned roles: Admin, Member, Contributor, Viewer.
# 
# Useful for segregating environments: Dev / Test / Prod workspaces.
# 
# ### 📦 Workspace Items Can Include:
#         - Lakehouses
# 
#         - Data Warehouses
#         
#         - Pipelines
#         
#         - Notebooks
#         
#         - Dataflows
#         
#         - Reports (Power BI)
#         
#         - Dashboards
# 
# ### ✅ Example:
# Contoso creates a "Finance Analytics" workspace where:
# 
#         - A lakehouse stores raw financial data
#         
#         - A pipeline ingests monthly Excel files
#         
#         - Reports display expense dashboards


# MARKDOWN ********************

# # 📦 4. Items (Artifacts)
# 
# 🧩 What are Items?
# Items are the individual data and analytics assets created and used within a workspace.
# 
# Think of them as the actual files, processes, or reports.
# 
# 🗂 Types of Items:
# | Item Type           | Description                                 |
# | ------------------- | ------------------------------------------- |
# | **Lakehouse**       | Combines data lake & data warehouse         |
# | **Dataflow Gen2**   | ETL processes (like Power Query)            |
# | **Pipeline**        | Orchestrates data movement & transformation |
# | **Notebook**        | Runs Spark code (PySpark, SQL, etc.)        |
# | **Data Warehouse**  | Traditional SQL-based analytics             |
# | **KQL DB**          | For log-style analytics                     |
# | **Power BI Report** | Data visualization                          |
# | **Semantic Model**  | Power BI model (previously datasets)        |


# MARKDOWN ********************

# ### ✅ Example:
# 
# Inside the "Finance Analytics" workspace:
# 
# Lakehouse1: Holds bank transactions
# 
# MonthlyETL Pipeline: Extracts files from SharePoint
# 
# FinanceReport: A Power BI dashboard visualizing spend

# MARKDOWN ********************

# ### 🧭 Visual Hierarchy Diagram (Text-Based)
# 
# [Microsoft Fabric Tenant: contoso.com]
# 
#        |
#        ├── Capacity: F4 (India Central)
#        |       ├── Workspace: Finance Analytics
#        |       |       ├── Lakehouse: FinanceLakehouse
#        |       |       ├── Pipeline: ETL_Monthly_Finance
#        |       |       └── Report: BudgetVsSpend
#        |
#        └── Capacity: Trial
#                ├── Workspace: HR Test Workspace
#                |       └── Notebook: AttritionAnalysis


# MARKDOWN ********************

# ### ✅ Summary Table
# | Level         | Description                        | Example                 |
# | ------------- | ---------------------------------- | ----------------------- |
# | **Tenant**    | Org-level container                | `contoso.com`           |
# | **Capacity**  | Resources for processing & storage | `F4`, `Trial`           |
# | **Workspace** | Team/project environment           | `Finance Analytics`     |
# | **Items**     | Actual artifacts & resources       | `Lakehouse`, `Pipeline` |


# MARKDOWN ********************

# ### 💡 Common Use Case Scenarios
# 1. Multi-Department Structure:
# 
#     - Tenant: Contoso Ltd.
#     
#     - Workspaces: HR, Finance, Marketing
# 
#     - Each uses shared or dedicated capacity depending on workload.
# 
# 2. .Development Lifecycle:
# 
# - Separate workspaces for:
# 
#         - Dev Workspace
# 
#         - Test Workspace
# 
#         - Prod Workspace
# 
# - Promotes modular development.
# 
# 3. Cost Optimization:
# 
#     - Use trial capacity for sandboxing.
# 
#     - Use dedicated capacity for production workloads.
