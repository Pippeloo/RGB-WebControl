# RGB-WebControl
## Info
This RGB webcontrol module can control WS2812b ledstrips.
The module is developed for the Raspberry Pi 4

## Connections
The following pins are available for use:
CH01 | CH02 | CH03 | CH04
-----|------|------|------
GPIO 18 | GPIO 21 | GPIO 12 | GPIO 10

## Commands
The commands have to be sent to the UDP port 5005 in json format.
### Info
| Value | Name | Values | Description |
|-------|------|--------|-------------|
|`debug`| Debug | `true` / `false` | Default: `false`|
|`ch`| Channel | `0` - `4`| Selects the channel to configure the data for |
|`p`| Pixels | `1` - `?`| Defines the amount of pixels have to be controlled on the ledstrip |
|`r`| Red | `0` - `255`| Sets this color of the ledstrip to the requested amount |
|`g`| Green | `0` - `255`| Sets this color of the ledstrip to the requested amount |
|`b`| Blue | `0` - `255`| Sets this color of the ledstrip to the requested amount |

### Examples
Enabeling debug mode:
`{ "debug" : "true" }`

Configuring Channel 1

`{ "ch" : "1", "p" : "50" }`

Setting the color to a rgb value

`{ "ch" : "1", "r" : "50", "g" : "100", "b" : "75" }`

**Note:** At this moment it is only possible to control **ONE** channel at a time.