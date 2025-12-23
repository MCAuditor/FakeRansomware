# 🚀 Quick Start Guide

## Prerequisites

Make sure you have Python installed:
```bash
python --version
```
You need **Python 3.7 or higher**.

## Testing the Simulation (2 Minutes)

### Option 1: Test French Version
```bash
python fake_ransomware_fr.py
```

### Option 2: Test English Version
```bash
python fake_ransomware_en.py
```

### 🔑 How to Exit
When the fullscreen simulation appears:
- Press **Ctrl+Shift+Q** simultaneously
- A dialog will appear explaining it was a test
- Click "Yes" to exit

⚠️ **Note**: You CANNOT close the window with the X button or Alt+F4 - only Ctrl+Shift+Q works!

---

## Creating an Executable (.exe)

If you want to create a standalone executable that doesn't require Python:

### Step 1: Install PyInstaller
```bash
pip install pyinstaller
```

### Step 2: Compile
**French version:**
```bash
pyinstaller --onefile --noconsole --name "FakeRansomware_FR" fake_ransomware_fr.py
```

**English version:**
```bash
pyinstaller --onefile --noconsole --name "FakeRansomware_EN" fake_ransomware_en.py
```

### Step 3: Find Your .exe
Look in the `dist/` folder that was created. Your executable will be there!

---

## Troubleshooting

**Problem**: `tkinter not found`  
**Solution**: Install tkinter:
- Windows: Reinstall Python with "tcl/tk" option checked
- Linux: `sudo apt-get install python3-tk`
- macOS: Should be included by default

**Problem**: Window doesn't go fullscreen  
**Solution**: This is normal in some environments. The program still works.

**Problem**: Can't exit the program  
**Solution**: Press **Ctrl+Shift+Q** (all three keys together)

---

## What You Have

✅ **fake_ransomware_fr.py** - French version of the simulation  
✅ **fake_ransomware_en.py** - English version of the simulation  
✅ **README.md** - Full documentation  
✅ **compile_instructions.txt** - Detailed compilation guide  
✅ **Icons** - For creating more realistic executables  

---

## Next Steps

1. ✅ Test both versions to see which you prefer
2. 📚 Read the full README.md for training best practices
3. 🔧 Compile to .exe if you want standalone executables
4. 🎓 Plan your security awareness training session
5. ⚖️ Get proper authorization before deploying!

**Ready to test? Run `python fake_ransomware_fr.py` now!**
