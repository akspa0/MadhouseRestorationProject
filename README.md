# Madhouse Restoration Project Tools

These are tools that we use to restore Madhouse Live shows!

---

* transcribeBites10-0.py - Dataset preparation tool, takes audio input and isolates speech then transcribes it using Google Speech-To-Text API (non-free)
* splitOrConcatAudio.py - (README_splitOrConcatAudio.md) - Dataset preparation tool, splits long audio inputs into 15 minute segments or concatenates them back into a single file.

---

We pre-process show audio into smaller 15 minute segments, to be processed through https://github.com/Anjok07/ultimatevocalremovergui with the 'best' Vocal models, then re-joined using the same script.
Vocal audio can then be processed into transcribed soundbites, if desired.

The datasets created with the transcribeBites script can be further augmented for voice cloning
