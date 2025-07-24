# 🖥️ AWS Cloud Optimizer

A simple Streamlit web app that connects to you AWS account and audits your running EC2 instances. It identifies optimization opportunities, such as underutilized instances, and displays the results in an easy-to-read report. 

---

# 🚀 Demo 

<img width="1138" height="250" alt="image" src="https://github.com/user-attachments/assets/6d3c94e1-bffb-4580-a663-f46cf1719342" />

<img width="885" height="233" alt="image" src="https://github.com/user-attachments/assets/89990e1e-cd4d-4b3d-9a1d-f759ac263481" />

Above you can see the corresponding output for no running instances. 

---

##  📦 Features 
- Uses boto3 to connect to AWS and fetch EC2 instance data 
- Displays real-time audit reports in the browser
- Informs if no running instances are found 
- Warns if instances are being underutilized 
- Lightweight UI built with Streamlit 

---

## 🛠 Requirements 
- Python 3
- Streamlit 
- boto3
- Pandas
- Verify AWS credentials, can do so by running: aws sso login 
- AWS credentials with permissions to run "ec2:DescribeInstances" 
    🔐 Setting Up Permissions in AWS
    1. Log into the AWS IAM Identiy Center 
    2. Ensure the correct region is selected
    3. Locate permission set (ex: amplify-policy)
    4. Scroll down to AWS managed policies and click "AmplifyBackendDeployFullAccess"
    5. Search for "AmazonEC2ReadOnlyAccess" and add this policy to user 

---

## 🔧 Setup & Run Instructions 

1. Clone the repo
2. Project Structure:
    - aws_cloud_optimizer (this is the folder in which everything is stored)
    - audit (folder) 
        - __init__.py (file)
        - ec2_audit.py (file)
    - app (folder)
        - __init__.py (file)
        - streamlit_app.py (file)
3. To run, type: streamlit run app/streamlit_app.py

---

# 🧠 Example Output 

If there are no running instances, you will see:
"No data found or no running instance." 
