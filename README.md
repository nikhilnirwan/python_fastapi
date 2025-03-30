1 . create env 1st
# command: python3 -m venv venv

2. activate environment
# source venv/bin/activate

3. deactivate environment
# deactivate

4. install dependency
pip install fastapi uvicorn pymongo

5. to run code use bellow command
uvicorn main:app --reload # reload every time if you change any file a single word



git setup in new project

echo "# python_fastapi" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/nikhilnirwan/python_fastapi.git
git push -u origin main