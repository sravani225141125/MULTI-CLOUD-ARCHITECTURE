# AWS Service Demo

This document explains how to deploy and run a Python Flask application on AWS EC2.

## Requirements
- AWS Account
- IAM user with EC2 permissions
- SSH key pair

## Steps

1. **Launch EC2 Instance**
   - Choose Ubuntu Server
   - Select t2.micro (Free tier)
   - Configure security group to allow port 22 (SSH) and 5000 (Flask app)

2. **Connect to EC2**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-public-ip
   ```

3. **Install Flask and Git**
   ```bash
   sudo apt update
   sudo apt install python3-pip git -y
   pip3 install flask
   ```

4. **Deploy Flask App**
   ```bash
   git clone https://github.com/YOUR_USERNAME/your-flask-repo.git
   cd your-flask-repo
   python3 app.py
   ```

5. **Access App**
   Visit `http://<EC2-PUBLIC-IP>:5000` in your browser.
