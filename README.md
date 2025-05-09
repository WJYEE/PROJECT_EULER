# 1. 로컬 git 초기화

git init

# 2. 파일 추가

git add .

# 3. 커밋

git commit -m "Initial commit with C++ Project Euler solution"

# 4. GitHub 레포 생성 후, 연결

git remote add origin https://github.com/your-username/your-repo.git

# 5. 푸시

git branch -M main
git push -u origin main

# C++ 컴파일 및 실행

g++ main.cpp -o main
./main
