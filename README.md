# ShortcutDeck

![Project Image Placeholder]()

A simple but powerful DIY macro keyboard featuring 12 hot-swappable keys (F13–F24) and a multifunctional rotary encoder. Built to be flexible, minimalistic, and open to modifications.

## 🎛️ Features

### 🔘 Rotary Encoder:
- **Right turn:** Volume up / Next track *(in Playback mode, only 1 command per 500ms)*
- **Left turn:** Volume down / Previous track *(same limitation)*
- **Single press:** Toggle Mute / Play-Pause
- **Double press:** Switch between Volume and Playback mode

### 🧷 Keys:
- 12 physical switches mapped to F13–F24
- Hot-swappable sockets for switch replacement
- Customizable keycaps (or printable)

---

## 🧰 Required Components

### ⚙️ Electronics:
- Raspberry Pi Pico (or compatible microcontroller — requires code & model adjustments)
- 1x Rotary Encoder (Keyes KY-040 recommended)
- 12x Mechanical switches (Kailh, Cherry MX, etc.)
- 12x Hot Swap sockets
- ~36x Dupont female connectors
- 13x 90° male Dupont connectors (or as needed for your microcontroller)
- Various pin Dupont connectors:  
  - 1x 7-pin  
  - 1x 6-pin  
  - 1x 5-pin  
  - 3x 4-pin  
  - 2x 2-pin  
  - 2x 1-pin
- 18x wires, 95mm each, 26AWG (~2m total)
- Soldering tools (iron, solder, flux)

### 🖨️ 3D Printed Parts:
- 1x Top enclosure
- 1x Bottom enclosure
- 1x Rotary knob (smooth or textured)
- 12x Keycaps *(optional, if you don't have your own)*
- 4x Rubber feet *(optional, or use adhesive furniture pads)*

### 🧪 PCB Fabrication:
- 1x 80x85mm single-sided copper board (cuprextit, 1.6mm thickness, 0.35µm copper layer)
- Ferric chloride etching solution
- PP plastic tray (flat, wide)
- Alcohol-based permanent marker (0.1–0.3mm tip)
- 0.8mm drill bit and bits for final hole sizes
- Sandpaper and alcohol for cleaning
- 4x Screws (1-2mm x 8-10mm)

---

## 🛠️ Building Process

### 1. PCB Manufacturing

1. Cut a piece of copper board to 80x85mm.
2. Print the PCB layout PDF and glue it onto the board with a glue stick.
   - Verify scale using the 14x14mm square marker.
3. Mark all required holes with a punch and peel off the paper.
4. Pre-drill holes using a 0.8mm bit, then finish with correct bit sizes.
5. Sand the surface and clean with alcohol.
6. Use the marker to trace traces and pads manually.
7. Heat the ferric chloride to ~50°C and pour into the tray.
8. Submerge the board for 10–20 minutes (monitor regularly).
9. Remove the ink with alcohol, inspect the traces, and measure resistance (target < 10kΩ).
10. Solder connectors.

### 2. Wiring and Controller Prep

- If your Pico has headers: gently remove the plastic spacer and bend pins 90° outward.
- If not: solder 90° male headers directly.
- Crimp and connect all Dupont cables exactly per the wiring diagram (match pinout carefully!).

### 3. Assembly

- Print all 3D parts in preferred material and color.
- Fit switches and sockets into the top cover.
- Attach the knob, rubber feet, and secure with 4 screws.

---

## 🧠 Programming

### CircuitPython:

1. Flash CircuitPython firmware to your Pico (see official [guide](https://circuitpython.org/board/raspberry_pi_pico/)).
2. Copy your Python code into `main.py` in the root of the Pico's USB drive.
3. Install required libraries inside the `/lib` folder.

### Debugging & Modding:
- Use **Thonny IDE** to upload, test or debug code via USB.
- Expect users to create their own forked versions – feel free to share!
