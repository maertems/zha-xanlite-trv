"""Quirk for Xanlite KZTETHEAU / Tuya TRV _TZE200_ytryxh0a.

Converted from zigbee-herdsman-converters definition.
Datapoint mapping follows the zigbee2mqtt definition.

Datapoints:
    DP 2: preset (auto=0, manual=1, holiday=2, comfort=3)
    DP 16: current_heating_setpoint (divideBy2 = 0.5°C steps)
    DP 24: local_temperature (divideBy10 = 0.1°C steps)
    DP 30: child_lock (on/off)
    DP 34: battery (voltage to percent)
    DP 45: error_status (raw)
    DP 101: comfort_temperature (divideBy2)
    DP 102: eco_temperature (divideBy2)
    DP 104: local_temperature_calibration (0.1°C steps)
    DP 105: holiday_temperature (divideBy2)
    DP 106: boost_heating (on/off)
    DP 107: window_detection (on/off)
    DP 116: open_window_temperature (divideBy2)
    DP 117: open_window_time (raw)
    DP 118: boost_time (countdown)
"""

import zigpy.types as t
from zigpy.quirks.v2 import EntityType
from zigpy.quirks.v2.homeassistant import UnitOfTemperature, UnitOfTime
from zigpy.quirks.v2.homeassistant.number import NumberDeviceClass
from zigpy.quirks.v2.homeassistant.sensor import SensorDeviceClass, SensorStateClass

from zhaquirks.tuya.builder import TuyaQuirkBuilder


class XanlitePreset(t.enum8):
    """Xanlite TRV preset modes."""

    Auto = 0x00
    Manual = 0x01
    Holiday = 0x02
    Comfort = 0x03


(
    TuyaQuirkBuilder("_TZE200_ytryxh0a", "TS0601")
    .friendly_name(
        model="KZTETHEAU",
        manufacturer="Xanlite",
    )
    # DP 2: Preset (auto, manual, holiday, comfort)
    .tuya_enum(
        dp_id=2,
        attribute_name="preset",
        enum_class=XanlitePreset,
        translation_key="preset",
        fallback_name="Preset",
    )
    # DP 16: Target temperature (current_heating_setpoint)
    .tuya_number(
        dp_id=16,
        attribute_name="current_heating_setpoint",
        type=t.uint16_t,
        device_class=NumberDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        min_value=5,
        max_value=30,
        step=0.5,
        multiplier=0.5,  # raw value * 0.5 = degrees
        entity_type=EntityType.STANDARD,
        translation_key="current_heating_setpoint",
        fallback_name="Target temperature",
    )
    # DP 24: Local temperature (raw value / 10 = °C) - READ ONLY sensor
    .tuya_sensor(
        dp_id=24,
        attribute_name="local_temperature",
        type=t.int16s,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        unit=UnitOfTemperature.CELSIUS,
        divisor=10,  # raw value / 10 = degrees
        translation_key="local_temperature",
        fallback_name="Current temperature",
    )
    # DP 30: Child lock
    .tuya_switch(
        dp_id=30,
        attribute_name="child_lock",
        entity_type=EntityType.CONFIG,
        translation_key="child_lock",
        fallback_name="Child lock",
    )
    # DP 34: Battery percentage
    .tuya_battery(dp_id=34)
    # DP 45: Error status
    .tuya_sensor(
        dp_id=45,
        attribute_name="error_status",
        type=t.uint8_t,
        entity_type=EntityType.DIAGNOSTIC,
        translation_key="error_status",
        fallback_name="Error status",
    )
    # DP 101: Comfort temperature (raw value / 2 = °C)
    .tuya_number(
        dp_id=101,
        attribute_name="comfort_temperature",
        type=t.uint16_t,
        device_class=NumberDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        min_value=5,
        max_value=30,
        step=0.5,
        multiplier=0.5,
        entity_type=EntityType.CONFIG,
        translation_key="comfort_temperature",
        fallback_name="Comfort temperature",
    )
    # DP 102: Eco temperature (raw value / 2 = °C)
    .tuya_number(
        dp_id=102,
        attribute_name="eco_temperature",
        type=t.uint16_t,
        device_class=NumberDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        min_value=5,
        max_value=30,
        step=0.5,
        multiplier=0.5,
        entity_type=EntityType.CONFIG,
        translation_key="eco_temperature",
        fallback_name="Eco temperature",
    )
    # DP 104: Local temperature calibration (raw value / 10 = °C)
    .tuya_number(
        dp_id=104,
        attribute_name="local_temperature_calibration",
        type=t.int16s,
        device_class=NumberDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        min_value=-9,
        max_value=9,
        step=0.1,
        multiplier=0.1,
        entity_type=EntityType.CONFIG,
        translation_key="local_temperature_calibration",
        fallback_name="Temperature calibration",
    )
    # DP 105: Holiday temperature
    .tuya_number(
        dp_id=105,
        attribute_name="holiday_temperature",
        type=t.uint16_t,
        device_class=NumberDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        min_value=0,
        max_value=30,
        step=0.5,
        multiplier=0.5,  # raw value * 0.5 = degrees
        entity_type=EntityType.CONFIG,
        translation_key="holiday_temperature",
        fallback_name="Holiday temperature",
    )
    # DP 106: Boost heating
    .tuya_switch(
        dp_id=106,
        attribute_name="boost_heating",
        entity_type=EntityType.STANDARD,
        translation_key="boost_heating",
        fallback_name="Boost heating",
    )
    # DP 107: Window detection
    .tuya_switch(
        dp_id=107,
        attribute_name="window_detection",
        entity_type=EntityType.CONFIG,
        translation_key="window_detection",
        fallback_name="Window detection",
    )
    # DP 116: Open window temperature (raw value / 2 = °C)
    .tuya_number(
        dp_id=116,
        attribute_name="open_window_temperature",
        type=t.uint16_t,
        device_class=NumberDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        min_value=5,
        max_value=25,
        step=0.5,
        multiplier=0.5,
        entity_type=EntityType.CONFIG,
        translation_key="open_window_temperature",
        fallback_name="Open window temperature",
    )
    # DP 117: Open window time (minutes)
    .tuya_number(
        dp_id=117,
        attribute_name="open_window_time",
        type=t.uint16_t,
        device_class=NumberDeviceClass.DURATION,
        unit=UnitOfTime.MINUTES,
        min_value=0,
        max_value=60,
        step=1,
        entity_type=EntityType.CONFIG,
        translation_key="open_window_time",
        fallback_name="Open window time",
    )
    # DP 118: Boost time remaining (seconds, countdown) - READ ONLY
    .tuya_sensor(
        dp_id=118,
        attribute_name="boost_time",
        type=t.uint16_t,
        device_class=SensorDeviceClass.DURATION,
        state_class=SensorStateClass.MEASUREMENT,
        unit=UnitOfTime.SECONDS,
        entity_type=EntityType.DIAGNOSTIC,
        translation_key="boost_time",
        fallback_name="Boost time remaining",
    )
    .skip_configuration()
    .add_to_registry()
)
