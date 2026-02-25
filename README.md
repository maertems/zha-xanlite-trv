# ZHA Quirk: Xanlite KZTETHEAU (Tuya TRV TS0601)

**ZHA** (Zigbee Home Automation) quirk for the **Xanlite KZTETHEAU** thermostatic radiator valve, based on the Tuya **TS0601** module (Zigbee model `_TZE200_ytryxh0a`).  
This quirk uses the **TuyaQuirkBuilder** (quirks v2) and exposes the device as **sensors**, **number entities**, and **switches** in Home Assistant — no Climate/Thermostat entity.

---

## Supported devices

| Brand / model | Zigbee identifier |
|---------------|--------------------|
| Xanlite KZTETHEAU | `_TZE200_ytryxh0a` + cluster `TS0601` |

---

## Functions and datapoints (Tuya)

The device communicates via Tuya **datapoints**. Mapping follows the [zigbee2mqtt](https://www.zigbee2mqtt.io/) definition (DP 16 = target temperature, DP 105 = holiday temperature). Source / device support request: [zigbee2mqtt issue #23079 — TRV ZIGBEE TS0601 / TZE200_ytryxh0a](https://github.com/Koenkk/zigbee2mqtt/issues/23079).

| DP | Role | Type | Entity in HA |
|----|------|------|--------------|
| **2** | Preset mode | Enum | Preset (auto, manual, holiday, comfort) |
| **16** | **Target temperature** | Value (÷2) | Target temperature (number) |
| **24** | Room temperature | Value (÷10) | Current temperature (sensor) |
| **30** | Child lock | Bool | Child lock (switch) |
| **34** | Battery | Value | Battery (sensor) |
| **45** | Error status | Value | Error status (diagnostic sensor) |
| **101** | Comfort temperature | Value (÷2) | Comfort temperature (number) |
| **102** | Eco temperature | Value (÷2) | Eco temperature (number) |
| **104** | Temperature calibration | Value | Temperature calibration (number) |
| **105** | Holiday temperature | Value (÷2) | Holiday temperature (number) |
| **106** | Boost heating | Bool | Boost heating (switch) |
| **107** | Window detection | Bool | Window detection (switch) |
| **116** | Open window temperature | Value (÷2) | Open window temperature (number) |
| **117** | Open window time | Value | Open window time (number, minutes) |
| **118** | Boost time remaining | Value | Boost time remaining (sensor, seconds) |

---

## Quirk implementation

The quirk is built with **TuyaQuirkBuilder** from `zhaquirks.tuya.builder` (quirks v2 API):

- **`XanlitePreset`** — Enum for preset modes: Auto, Manual, Holiday, Comfort.
- **TuyaQuirkBuilder** — Declares each datapoint as a `.tuya_sensor()`, `.tuya_number()`, `.tuya_switch()`, or `.tuya_enum()` with the appropriate device class, unit, min/max, and multiplier/divisor. The builder registers the quirk with `.add_to_registry()`.

Value conversions (e.g. raw ÷ 2 for °C, ÷ 10 for 0.1°C) are handled via `multiplier` / `divisor` in the builder.

---

## Installation in Home Assistant

**ZHA** (Zigbee Home Automation integration) must be installed and configured.

1. **Edit `configuration.yaml`** (in your Home Assistant config directory) and add under the `zha:` key:

   ```yaml
   zha:
     enable_quirks: true
     custom_quirks_path: /config/quirks
   ```

   If you already have a `zha:` block, add only `enable_quirks: true` and `custom_quirks_path: /config/quirks` under it.

2. **Create the `quirks` directory** at the root of your Home Assistant config:
   - On **Home Assistant OS** (SSH): the config root is typically `/config/`, so create `/config/quirks/`.
   - If you access the host filesystem (e.g. via SSH as root), the config is often at `/root/homeassistant/` (or under the path shown in the HA docs for your installation). Create the folder `quirks` at that config root (e.g. `/root/homeassistant/quirks/`).

3. **Copy the quirk file** `ts0601_xanlite_trv.py` into the `quirks` directory.

4. **Restart Home Assistant** so the configuration and custom quirks are loaded.

---

## After installation

1. **Re-pair the device** (or remove and re-add it in ZHA) so the quirk is applied.
2. In Home Assistant you should see **sensors** (current temperature, battery, error status, boost time), **number** entities (target temperature, holiday/comfort/eco temps, calibration, open window temp/time), and **switches** (child lock, boost heating, window detection), plus the **Preset** enum — no Climate card.

---

## This repository

This repository contains the quirk file and this documentation. To use it in Home Assistant, follow the installation steps above (custom quirks path and `quirks` directory).

---

## References

- **zigbee2mqtt (device support):** [Issue #23079 — TRV ZIGBEE TS0601 / TZE200_ytryxh0a](https://github.com/Koenkk/zigbee2mqtt/issues/23079)

---

## License

See the [zha-device-handlers](https://github.com/home-assistant/zha-device-handlers) repository for the license used by ZHA quirks. This quirk follows the same terms.
