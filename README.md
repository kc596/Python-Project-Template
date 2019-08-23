# Template for python projects

### Running project
1. Install python3
2. Create virtual environment and activate it (recommended). 
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install requirements. Goto root of the project and run the command.
   ```
   python3 -m pip install -r requirements.txt
   ```
4. Set environment variables `PROJECT_ALIAS_PROFILE` and `PROJECT_ALIAS_CONFIG_PATH` as defined in `constants.py`
   ```
   export PROJECT_ALIAS_PROFILE=prod
   export PROJECT_ALIAS_CONFIG_PATH=config/ 
   ```
5. Start the project.
    ```
    python3 -m src.main
    ```