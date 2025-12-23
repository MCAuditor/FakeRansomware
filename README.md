# 🛡️ Fake Ransomware - Cybersecurity Awareness Training Tool

## ⚠️ IMPORTANT DISCLAIMER

**THIS IS A SIMULATION TOOL FOR EDUCATIONAL PURPOSES ONLY**

This application is a **harmless** ransomware simulator designed exclusively for authorized cybersecurity awareness training in corporate and institutional environments.

### What This Tool Does NOT Do:
- ❌ Does NOT encrypt any files
- ❌ Does NOT damage or modify data
- ❌ Does NOT contain malicious code
- ❌ Does NOT communicate with external servers
- ❌ Does NOT pose any actual threat to systems

### Authorized Use Only:
✅ Security awareness training sessions  
✅ Cybersecurity education programs  
✅ Controlled corporate training environments  
✅ With proper authorization and participant consent

## 🎯 Purpose

This tool simulates a realistic ransomware attack screen to:
- Raise awareness about ransomware threats
- Test employee response to security incidents
- Demonstrate the appearance of real ransomware attacks
- Educate staff on warning signs and prevention methods
- Encourage better cybersecurity practices

## 🌍 Language Support

The tool is available in two language versions:
- **French**: `fake_ransomware_fr.py` - Interface en français
- **English**: `fake_ransomware_en.py` - English interface

## ✨ Features

- 🖥️ **Fullscreen Simulation**: Realistic ransomware interface that takes over the screen
- 💰 **Fake Bitcoin Demand**: Displays a randomly generated Bitcoin address and payment instructions
- ⏱️ **Real Countdown Timer**: 72-hour countdown timer that actually counts down
- 🔑 **Unique Victim ID**: Generates a unique identifier for each "victim"
- 🚪 **Safe Exit**: Hidden exit method via `Ctrl+Shift+Q` keyboard combination
- 🎨 **Professional Design**: Dark red interface with skull icon for realistic appearance
- 🔒 **Fullscreen Lock**: Prevents easy closing to simulate real ransomware behavior

## 📋 Requirements

### Python Environment:
```
Python 3.7 or higher
tkinter (included with most Python installations)
```

### For Compilation (Optional):
```
pyinstaller (to create standalone executables)
```

## � Setup Virtual Environment (Recommended)

It's recommended to use a virtual environment to keep dependencies isolated:

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install PyInstaller (if you want to compile)
pip install pyinstaller
```

**Linux/macOS:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install PyInstaller (if you want to compile)
pip install pyinstaller
```

**To deactivate the virtual environment when done:**
```bash
deactivate
```

## �🚀 How to Use

### Method 1: Run Python Script Directly

**French Version:**
```bash
python fake_ransomware_fr.py
```

**English Version:**
```bash
python fake_ransomware_en.py
```

### Method 2: Create Standalone Executable

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Compile to Executable:**
   
   For French version:
   ```bash
   pyinstaller --onefile --noconsole --icon=icons8-photos-96.ico --name "FakeRansomware_FR" fake_ransomware_fr.py
   ```
   
   For English version:
   ```bash
   pyinstaller --onefile --noconsole --icon=icons8-photos-96.ico --name "FakeRansomware_EN" fake_ransomware_en.py
   ```
   
   **Note:** The `--icon` parameter makes the executable appear as a photo/image file, making it more convincing for training purposes.

3. **Find Your Executable:**
   The compiled `.exe` file will be located in the `dist/` folder.

### You can even hide the .exe file in an image,pdf,word file etc...

For hiding the .exe file in the image I used winrar but there are other ways with other tools.

## 🔑 Exit Instructions

When the simulation is running:
1. Press **`Ctrl+Shift+Q`** simultaneously
2. A dialog box will appear explaining this was a security awareness test
3. Confirm to close the application

**Note:** The exit instructions are hidden at the bottom of the screen (same color as background).

## 📚 Training Best Practices you can do

### Before Deployment:
1. ✅ Obtain written authorization from management
2. ✅ Inform IT/Security team of the planned exercise
3. ✅ Prepare training materials for post-exercise debrief
4. ✅ Plan timing to minimize business disruption
5. ✅ Have support staff ready to assist confused employees

### During Deployment:
1. 🎯 Monitor employee reactions and response times
2. 📝 Document who encounters the simulation
3. ⏰ Don't leave the simulation running too long
4. 🆘 Have IT support available for questions

### After Deployment:
1. 📊 Conduct immediate debrief session
2. 🎓 Provide cybersecurity training
3. 🔍 Explain warning signs they should have noticed
4. 💡 Share best practices for ransomware prevention
5. 📖 Distribute educational materials
6. 🔄 Follow up with additional training if needed

## 🛡️ What Employees Should Learn

This simulation teaches users to:
- 🚨 Recognize ransomware attack patterns
- 📧 Be cautious with email attachments and links
- 🔍 Verify sender identities before opening files
- 📎 Check file extensions (e.g., `.exe` disguised as documents)
- 🆘 Report suspicious activity to IT/Security immediately
- 💾 Understand the importance of regular backups
- 🔒 Practice safe computing habits
- ⚡ Respond quickly to potential security incidents

## 📁 Project Structure

```
FakeRansomware/
├── README.md                          # This file
└── Ranstest/
    ├── fake_ransomware_fr.py         # French version
    ├── fake_ransomware_en.py         # English version
    ├── compile_instructions.txt      # Compilation guide
    └── *.spec                        # PyInstaller specifications
```

## ⚖️ Legal Notice

### Important Legal Information:

- **Authorized Use Only**: This tool must only be used with explicit written authorization
- **No Unauthorized Deployment**: Deploying this tool without authorization may violate:
  - Computer Fraud and Abuse Act (CFAA) in the United States
  - Computer Misuse Act in the United Kingdom
  - Similar laws in other jurisdictions
- **Liability**: The creator assumes NO LIABILITY for any misuse, unauthorized use, or consequences arising from the use of this tool
- **Professional Use**: Intended for professional security trainers and IT departments only
- **Participant Consent**: Ensure proper consent and authorization before use in any organization

**WARNING**: Misuse of this tool could result in:
- Criminal charges
- Civil liability
- Employment termination
- Damage to professional reputation

## 🤝 Responsible Disclosure

If you discover any security issues or ways this tool could be misused, please report them responsibly to the project maintainer.

## 📞 Support & Questions

For authorized security training questions or implementation guidance:
- Review the documentation in this README
- Check the compilation instructions in `Ranstest/compile_instructions.txt`
- Ensure you have proper authorization before deployment

## 🎓 Additional Resources

**Recommended Reading:**
- NIST Cybersecurity Framework
- SANS Security Awareness Training materials
- CISA Ransomware Guide
- Your organization's security policies

**Real Ransomware Prevention:**
- Maintain regular, offline backups
- Keep systems and software updated
- Use antivirus/anti-malware solutions
- Implement email filtering
- Train employees regularly
- Use principle of least privilege
- Enable multi-factor authentication

---

## ⚡ Remember

**This is ONLY a training tool. Real ransomware causes real, devastating damage to individuals and organizations.**
