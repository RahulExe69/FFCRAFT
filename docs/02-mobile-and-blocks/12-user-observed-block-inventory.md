# User-observed Craftland block inventory (draft)

> **Provenance:** normalized from Rahul's original [`Rough.txt`](../Rough.txt). That file is intentionally preserved and must not be overwritten. This catalogue retains reported block signatures, not claims that every block is current or available in every context.

## How to use this catalogue

- Treat each signature as a **user-observed editor transcription** until checked against current official docs or the installed editor.
- Keep spellings exactly as recorded in the raw file when matching; put corrections in separate verified-name fields later rather than silently changing the source.
- Verify every block's script context, server/client status, Craftland Mobile vs Studio PC support, exact parameter types, return values, and deprecation status before generating implementation code.
- The extraction is heuristic; narrative details and explanatory context remain in `Rough.txt`.

## Primary official references

- [Block Scripts and parameter slots](https://ffcraftland.garena.com/en/tutorial/cl/4-101)
- [API reference](https://ffcraftland.garena.com/en/docs/api)
- [Event reference](https://ffcraftland.garena.com/en/docs/event/)
- [Type reference](https://ffcraftland.garena.com/en/docs/type)
- [Enum reference](https://ffcraftland.garena.com/en/docs/enum)
- [Craftland Studio PC code scripts](https://ffcraftland.garena.com/en/tutorial/fe/1-9)

## Summary

- Extracted sections: **35**
- Candidate block/component lines indexed: **443**
- Enum-like dropdown types recorded: **65**
- Original source lines: **677**

These are counts of the automated draft inventory, not counts of official APIs or fully verified blocks.

## Top-level categories described by the author

| Category | Coverage |
|---|---|
| EVENT | Global and private events; custom events are user-created |
| ACTION | Std Library, Scene, Level Object, Items, UI, Combat, Playable, AI, Behaviour Tree, Other |
| GAME | Global, Player, Team, Physics, Camera, Workflow, Economy, Minimap, Animation, Collection, Story, Other |
| DATA | Basic, Math, List, Dictionary (label uncertain), Vector, Strings, Convert, Enum |
| LOGIC | If/else, if, conditional loop, integer range loop, loop over elements, continue, break |
| VAR | Bool, Int, Float, String, Vector2, Vector3, Any Type |
| FUNC | Functions are mentioned; full function-creation details are not included |

## Scope observations recorded in Rough.txt

- **Global:** the author reports global variables/functions can be used across player, team, object, HUD, and trigger script editors.
- **Player:** the author reports player-local variables/functions are usable in player scope.
- **Individual object/HUD/trigger scripts:** the author reports variables/functions created there are local to that specific script.
- **Verification needed:** confirm these access rules in the target editor version; don't infer PC code-script visibility rules directly from block scripting.

## Extracted block/component candidates by section

### EVENT — GLOBAL EVENT

- **On Game Start** — `On Game Start` _(Rough.txt line 24; unverified)_
- **On Round Start (Round Index)** — `On Round Start (Round Index)` _(Rough.txt line 25; unverified)_
- **On Round End (Round Index)** — `On Round End (Round Index)` _(Rough.txt line 26; unverified)_
- **On Phase Start (Phase)** — `On Phase Start (Phase)` _(Rough.txt line 27; unverified)_
- **On Phase End (Phase)** — `On Phase End (Phase)` _(Rough.txt line 28; unverified)_
- **On Player Quit Midway (Player)** — `On Player Quit Midway (Player)` _(Rough.txt line 29; unverified)_
- **On Player Be Eliminated (Player)** — `On Player Be Eliminated (Player)` _(Rough.txt line 30; unverified)_
- **On Player Assist (Assist Player, Eliminated Player)** — `On Player Assist (Assist Player, Eliminated Player)` _(Rough.txt line 31; unverified)_
- **On Player Deal Damage (Attacker, Target, Damage Type, Damage, Damaged Body Part)** — `On Player Deal Damage (Attacker, Target, Damage Type, Damage, Damaged Body Part)` _(Rough.txt line 32; unverified)_
- **On Player Eliminate (Player, Eliminated Player)** — `On Player Eliminate (Player, Eliminated Player)` _(Rough.txt line 33; unverified)_
- **On Player Join (Player)** — `On Player Join (Player)` _(Rough.txt line 34; unverified)_
- **On Player Revived (Player, Revival Source)** — `On Player Revived (Player, Revival Source)` _(Rough.txt line 35; unverified)_
- **On Team Ace (Team)** — `On Team Ace (Team)` _(Rough.txt line 36; unverified)_
- **On Camera Raycast** — `On Camera Raycast (Player, Is Hit, Hit Position, Camera Direction, Camera Position, Hit Entity)` _(Rough.txt line 37; unverified)_
- **On Fixed Update** — `On Fixed Update` _(Rough.txt line 38; unverified)_
- **On Game Pause** — `On Game Pause` _(Rough.txt line 39; unverified)_
- **On Game Resume** — `On Game Resume` _(Rough.txt line 40; unverified)_
- **On User Quit or User Match End (Player)** — `On User Quit or User Match End (Player)` _(Rough.txt line 41; unverified)_

### EVENT — PRIVATE EVENT

- **On Awake** — `On Awake` _(Rough.txt line 45; unverified)_
- **On Update** — `On Update` _(Rough.txt line 46; unverified)_
- **On Destroy** — `On Destroy` _(Rough.txt line 47; unverified)_
- **On Enable** — `On Enable` _(Rough.txt line 48; unverified)_
- **On Disable** — `On Disable` _(Rough.txt line 49; unverified)_
- **On Eliminate (Target, Damaged Body Part)** — `On Eliminate (Target, Damaged Body Part)` _(Rough.txt line 50; unverified)_
- **On Eliminated (Attacker, Damage Type, Damage Body Part)** — `On Eliminated (Attacker, Damage Type, Damage Body Part)` _(Rough.txt line 51; unverified)_
- **On Take Damage (Attacker, Damage Type, Damage, Damaged Body Part)** — `On Take Damage (Attacker, Damage Type, Damage, Damaged Body Part)` _(Rough.txt line 52; unverified)_
- **On Deal Damage (Target, Damage Type, Damage, Damaged Body Part)** — `On Deal Damage (Target, Damage Type, Damage, Damaged Body Part)` _(Rough.txt line 53; unverified)_
- **On Equip Weapon (Weapon)** — `On Equip Weapon (Weapon)` _(Rough.txt line 54; unverified)_
- **On Equip Armor (Equipment ID)** — `On Equip Armor (Equipment ID)` _(Rough.txt line 55; unverified)_
- **On User Consumable (ConsumableID, Item, Spawned Item)** — `On User Consumable (ConsumableID, Item, Spawned Item)` _(Rough.txt line 56; unverified)_
- **On Access Item (Item ID, Item)** — `On Access Item (Item ID, Item)` _(Rough.txt line 57; unverified)_
- **On Access Weapon (Weapon)** — `On Access Weapon (Weapon)` _(Rough.txt line 58; unverified)_
- **On Revived (Revival Source)** — `On Revived (Revival Source)` _(Rough.txt line 59; unverified)_
- **On Drop Weapon (Weapon)** — `On Drop Weapon (Weapon)` _(Rough.txt line 60; unverified)_
- **On Drop Consumable (ConsumableID, Item)** — `On Drop Consumable (ConsumableID, Item)` _(Rough.txt line 61; unverified)_
- **On Aiming (Target)** — `On Aiming (Target)` _(Rough.txt line 62; unverified)_
- **On Aimed (Player)** — `On Aimed (Player)` _(Rough.txt line 63; unverified)_
- **On Hit By Bullet (Weapon, Hit Position)** — `On Hit By Bullet (Weapon, Hit Position)` _(Rough.txt line 64; unverified)_
- **On Disconnect (Player)** — `On Disconnect (Player)` _(Rough.txt line 65; unverified)_
- **On Reconnect (Player)** — `On Reconnect (Player)` _(Rough.txt line 66; unverified)_
- **On Attack** — `On Attack` _(Rough.txt line 67; unverified)_
- **On Crouch** — `On Crouch` _(Rough.txt line 68; unverified)_
- **On Prone** — `On Prone` _(Rough.txt line 69; unverified)_
- **On Jump** — `On Jump` _(Rough.txt line 70; unverified)_
- **On Sprint** — `On Sprint` _(Rough.txt line 71; unverified)_
- **On Enter Vehicle (Vehicle)** — `On Enter Vehicle (Vehicle)` _(Rough.txt line 72; unverified)_
- **On Leave Vehicle (Vehicle)** — `On Leave Vehicle (Vehicle)` _(Rough.txt line 73; unverified)_
- **On Drive Vehicle (Vehicle)** — `On Drive Vehicle (Vehicle)` _(Rough.txt line 74; unverified)_
- **On User Portal (Portal)** — `On User Portal (Portal)` _(Rough.txt line 75; unverified)_
- **On Bounced by Tire (Tire)** — `On Bounced by Tire (Tire)` _(Rough.txt line 76; unverified)_
- **On Hit Fly (Mechanism)** — `On Hit Fly (Mechanism)` _(Rough.txt line 77; unverified)_
- **On Throwable Explodes (Hit Position)** — `On Throwable Explodes (Hit Position)` _(Rough.txt line 78; unverified)_
- **On Pre Take Damage (Attacker, Damage Type, Damage, Damaged Body Part)** — `On Pre Take Damage (Attacker, Damage Type, Damage, Damaged Body Part)` _(Rough.txt line 79; unverified)_
- **On Pre Deal Damage (Target, Damage Type, Damage, Damaged Body Part)** — `On Pre Deal Damage (Target, Damage Type, Damage, Damaged Body Part)` _(Rough.txt line 80; unverified)_
- **On Switch Handheld (Item)** — `On Switch Handheld (Item)` _(Rough.txt line 81; unverified)_
- **On Access Equipment (Item)** — `On Access Equipment (Item)` _(Rough.txt line 82; unverified)_
- **On Move (Pose)** — `On Move (Pose)` _(Rough.txt line 83; unverified)_
- **On Idle (Pose)** — `On Idle (Pose)` _(Rough.txt line 84; unverified)_
- **On Standup (Pre Pose)** — `On Standup (Pre Pose)` _(Rough.txt line 85; unverified)_
- **On Surfing** — `On Surfing` _(Rough.txt line 86; unverified)_
- **On Surfing Stop** — `On Surfing Stop` _(Rough.txt line 87; unverified)_
- **On Sprint Stop** — `On Sprint Stop` _(Rough.txt line 88; unverified)_
- **On Jump Stop** — `On Jump Stop` _(Rough.txt line 89; unverified)_
- **On Be Knocked Down (Attacker)** — `On Be Knocked Down (Attacker)` _(Rough.txt line 90; unverified)_
- **On Change Team (Former Team, Current Team)** — `On Change Team (Former Team, Current Team)` _(Rough.txt line 91; unverified)_
- **On Plot Start (Plot ID)** — `On Plot Start (Plot ID)` _(Rough.txt line 92; unverified)_
- **On Plot End (Plot ID)** — `On Plot End (Plot ID)` _(Rough.txt line 93; unverified)_
- **On Trigger Plot Option (Plot ID, Option ID)** — `On Trigger Plot Option (Plot ID, Option ID)` _(Rough.txt line 94; unverified)_
- **here we have script blocks component blocks which we adds to other and another blocks can be added under them, I can't explain it so hard so here's an examples** — `here we have script blocks component blocks which we adds to other and another blocks can be added under them, I can't explain it so hard so here's an examples= Set Property: 'Entity' ___ 'Entity' --- 'Set Property' --- 'Operation' = ___      so here this cotation 'Entity' and others in cotation is in low colour texture means it's telling us what to put or set in __ and --- and ____ means a box where we can add components like get Property block and those and ---- means drop down menu from where we can choose the appropriate option of the component we want to manage so here we go this is gonna be hard to understand but ig you can do it` _(Rough.txt line 108; unverified)_

### ACTION — STD LIBRARY

- **Set Property** — `Set Property: Entity ___ Entity --- Set Property --- Operation = ___ (so suppose at first drop menu i add player then in the 1st drop down i have to select player entity then in the second drop down i can select what to edit like hp position orientation knockout state etc. like that we can also set property of othe entity and assets and everything)` _(Rough.txt line 112; unverified)_
- **Get Property** — `.Get Property: Entity ___ Entity --- Set Property ---` _(Rough.txt line 113; unverified)_
- **Get Global** — `.Get Global` _(Rough.txt line 114; unverified)_
- **Log Info** — `Log Info: Content ___` _(Rough.txt line 115; unverified)_
- **Get All Players** — `.Get All Players` _(Rough.txt line 116; unverified)_
- **Get All Teams** — `.Get All Teams` _(Rough.txt line 117; unverified)_
- **Wait for Milliseconds** — `Wait for Milliseconds: Duration (ms)  0` _(Rough.txt line 118; unverified)_
- **Wait For Next Frame** — `.Wait For Next Frame` _(Rough.txt line 119; unverified)_
- **This Entity** — `.This Entity` _(Rough.txt line 120; unverified)_
- **Type As ---** — `.Type As --- (this one is to change type suppose I created a variable and made like at spawn that when player joins the match convert triggering Modify: Player 1 as Triggering Player so in other block where there is ___ so if I add Player 1 variable there it'll not add so there we have to add this block and select Player Entity from --- to make the engine think Player 1 is a player entity)` _(Rough.txt line 121; unverified)_
- **Get Type** — `.Get Type: Target ___` _(Rough.txt line 122; unverified)_
- **Type Is** — `.Type Is: Target ___ Type ___` _(Rough.txt line 123; unverified)_
- **Is Sub Type Of** — `.Is Sub Type Of: Target ___ Type ___` _(Rough.txt line 124; unverified)_
- **Filter Entity** — `.Filter Entity: Must___ Not___ Any___` _(Rough.txt line 125; unverified)_
- **Destroy** — `Destroy: Target ___` _(Rough.txt line 126; unverified)_
- **Add Tag** — `Add Tag: Target ___ Custom Tag _please enter the content` _(Rough.txt line 127; unverified)_
- **Remove Tag** — `Remove Tag: Target ___ Custom Tag   please enter the content` _(Rough.txt line 128; unverified)_
- **Has Tag** — `Has Tag: Target ___ Custom Tag   please enter the content` _(Rough.txt line 129; unverified)_
- **Set Active** — `Set Active: Target ___ Active ---- (this one actually has true/false in the drop down menu so if any one has that thein I'll write them like this .----tf )` _(Rough.txt line 130; unverified)_
- **Set Parent** — `Set Parent: Parent ___ Child ___ World Position Stays --- (generally it comes with tf but we can change the component and use get property to fetch other's position maybe idk)` _(Rough.txt line 131; unverified)_
- **Progressive Movement Property** — `Progressive Movement Property: Entity ___ Entity --- Set Property --- Value ___` _(Rough.txt line 132; unverified)_
- **Get Server Region** — `.Get Server Region` _(Rough.txt line 133; unverified)_
- **Clear All Children** — `Clear All Children: Parent ___` _(Rough.txt line 134; unverified)_
- **Get Children By Index** — `.Get Children By Index: Parent ___ Index . 0  (I used . Before 0 means it's also a component, comp inside comp)` _(Rough.txt line 135; unverified)_
- **Get Children** — `.Get Children :Parent ___` _(Rough.txt line 136; unverified)_
- **Get Parnt** — `.Get Parnt: Child ___` _(Rough.txt line 137; unverified)_
- **Profanity Filter** — `.Profanity Filter: Content   please enter the content` _(Rough.txt line 138; unverified)_
- **Create Bot** — `Create Bot: Difficulty ___ Team Sequency . 0  Return (Created Entity)` _(Rough.txt line 139; unverified)_
- **Destroy Bot** — `Destroy Bot: Target ___` _(Rough.txt line 140; unverified)_
- **Log Warning** — `Log Warning: Content ___` _(Rough.txt line 141; unverified)_
- **Log Error** — `Log Error: Content ___` _(Rough.txt line 142; unverified)_
- **Has Component** — `.Has Component: Target ___ Component ___` _(Rough.txt line 143; unverified)_
- **Get Child By Name** — `.Get Child By Name: Parent ___ Name  please enter the content` _(Rough.txt line 144; unverified)_
- **Add Comment** — `Add Comment: Content  please enter the content` _(Rough.txt line 145; unverified)_
- **Get Type Name** — `.Get Type Name: Target ___` _(Rough.txt line 146; unverified)_

### ACTION — SCENE

- **Set SkyBox Type ---- (it's for changing sky box by selecting from drop down menu)** — `Set SkyBox Type ---- (it's for changing sky box by selecting from drop down menu)` _(Rough.txt line 152; unverified)_

### ACTION — LEVEL OBJECT

- **Create Level Object** — `Create Level Object: Position .XYZ Level Object --- (Created Entity) {here level object means yk all type of objects or assets that available in the game which we can create and tbh I don't use it to create object, I prefer to place object visually because it's easier if I want to code in those objects}` _(Rough.txt line 160; unverified)_
- **Filter Level Object** — `.Filter Level Object: Filter Type ---` _(Rough.txt line 161; unverified)_
- **SpawnNextWave** — `SpawnNextWave: Target ___` _(Rough.txt line 162; unverified)_
- **Clone** — `Clone: Target .No entity  (Created Entity) {Here no Entity means by clicking on it it'll let us select level object from the map and let us copy them and also using that No entity block we can also set or get their property using property blocks too}` _(Rough.txt line 163; unverified)_
- **Enter Vehicle** — `Enter Vehicle: Player ___ Vehicle ___ Seat ---- (Is Success)` _(Rough.txt line 164; unverified)_
- **Create Air Drop (Created Entity)** — `Create Air Drop (Created Entity)` _(Rough.txt line 165; unverified)_
- **Start Parachute** — `Start Parachute: Target ___ Forced Parachute Height  0  Surfing Max. Speed ___ Diving Max. Speed ___ Parachuting Max. Speed ___` _(Rough.txt line 166; unverified)_

### ACTION — ITEMS

- **Add Item** — `Add Item : Target ___ Item --- Count  0  (Created Entity) { here in the drop down menu, all the available in game items are available from attachment to consumable and to guns and everything of the game we can select that from there}` _(Rough.txt line 172; unverified)_
- **Create Item In Scene** — `Create Item In Scene: Position .XYZ items --- Counts  0` _(Rough.txt line 173; unverified)_
- **Destroy Target** — `Destroy Target: Target ___ Item ___ Count  0` _(Rough.txt line 174; unverified)_
- **Set Pickup Status** — `Set Pickup Status: Target ___ Is Disabled .---- tf` _(Rough.txt line 175; unverified)_
- **Set Drop Status** — `Set Drop Status: Target ___ Is Disabled .---- tf` _(Rough.txt line 176; unverified)_
- **Clear Backpack** — `Clear Backpack: Target ___` _(Rough.txt line 177; unverified)_
- **Get Item Count** — `.Get Item Count: Target ___ Item ___` _(Rough.txt line 178; unverified)_
- **Destroy Equipment** — `Destroy Equipment: Target ___ Slot --- Count _0_ (Is Success)` _(Rough.txt line 179; unverified)_
- **Clear Residual Level Objects** — `Clear Residual Level Objects` _(Rough.txt line 180; unverified)_
- **Switch Weapon** — `Switch Weapon: Target ___ Slot ___ (Is Success)` _(Rough.txt line 181; unverified)_
- **Set Special Item Status** — `Set Special Item Status: Target ___ Item --- Status ---tf (Created Entity)` _(Rough.txt line 182; unverified)_
- **Get Consumables** — `Get Consumables: Target ___(Result)` _(Rough.txt line 183; unverified)_
- **Add Attachment** — `Add Attachment: Target ___ Slot ___ Item ___ (Is Success, Attachment)` _(Rough.txt line 184; unverified)_
- **Get Equipment** — `Get Equipment: Target ___ Slot ___ (Equipments, Attachments)` _(Rough.txt line 185; unverified)_
- **Drop Item** — `Drop Item: Target ___ Item ___` _(Rough.txt line 186; unverified)_

### ACTION — UI

- **Create Built in UI** — `Create Built in UI: Target ___ Type ___ (Created Entity)` _(Rough.txt line 192; unverified)_
- **Create Custom HUD** — `Create Custom HUD: Player ___ HUD Index --- (Interface Entity)` _(Rough.txt line 193; unverified)_
- **Get Widget From Custom UI** — `.Get Widget From Custom UI: Target ___ Custom UI --- Widget ID ---` _(Rough.txt line 194; unverified)_
- **Get Widget By Path** — `.Get Widget By Path: Owner ___ Target ___ Path  please enter the content` _(Rough.txt line 195; unverified)_
- **Create Custom UI Widget** — `Create Custom UI Widget: Widget Type --- UI ___ Parent Widget ___ (Created Entity)` _(Rough.txt line 196; unverified)_
- **Set Widget Parent** — `Set Widget Parent: Parent ___ Child ___` _(Rough.txt line 197; unverified)_
- **Notify Show Tips** — `Notify Show Tips: Target ___ Content ___ Colour ___ Duration (ms)  0` _(Rough.txt line 198; unverified)_

### ACTION — COMBAT

- **Deal Damage** — `Deal Damage: Target ___ Type --- Damage _0_` _(Rough.txt line 204; unverified)_
- **Deal Damage** — `Deal Damage: Target ___ Attacker ___ Type --- Damage _0_` _(Rough.txt line 205; unverified)_

### ACTION — PLAYABLE

- **Reset** — `Reset: Target ___` _(Rough.txt line 211; unverified)_
- **Play** — `Play: Target ___ Reset ---tf` _(Rough.txt line 212; unverified)_
- **Pause** — `Pause: Target ___` _(Rough.txt line 213; unverified)_
- **Create Trajectory** — `Create Trajectory: Target ___ Initial Velocity .XYZ Acceleration .XYZ Max. Displacement  0  Auto Play ---tf (Created Entity)` _(Rough.txt line 214; unverified)_
- **Create Follow** — `Create Follow: Target ___ Follow Target ___ Offset .XYZ Cordinate System ___ Auto Play ---tf (Created Entity)` _(Rough.txt line 215; unverified)_
- **Create Look At** — `Create Look At: Target ___ Look At Target ___ Offset .XYZ Cordinate System ___ Auto Play ---tf (Created Entity)` _(Rough.txt line 216; unverified)_
- **Sample On Curve** — `.Sample On Curve: Curve ___ Sample Point  0` _(Rough.txt line 217; unverified)_
- **Get Result From Curve** — `.Get Result From Curve: Value Type ___ Source Value ___ Destination Value ___  Curve ___ Sample Point  0` _(Rough.txt line 218; unverified)_
- **Create Sound** — `Create Sound: Target ___ Resource ___ Loop Type ___ Auto Play ---tf (Created Entity)` _(Rough.txt line 219; unverified)_
- **Create Effect** — `Create Effect: Target ___ Resource ___ Loop Type ___ Auto Play ---tf (Created Entity)` _(Rough.txt line 220; unverified)_
- **Create Along Path Motion** — `Create Along Path Motion: Target ___ Path ___ Style ___ Speed . 0  Tangent Facing ---tf Auto Play ---tf (Created Entity)` _(Rough.txt line 221; unverified)_
- **Notify Play Sound** — `Notify Play Sound: Target ___ Resource ___ Speed . 0` _(Rough.txt line 222; unverified)_

### ACTION — AI

- **Enable Default Behaviour Tree** — `Enable Default Behaviour Tree : Target ___ Enable ---tf` _(Rough.txt line 228; unverified)_
- **Pursuit Target** — `Pursuit Target: Target ___ Pursuit Target ___` _(Rough.txt line 229; unverified)_
- **Patrol To** — `Patrol To: Target ___ Position .XYZ Come Back ---tf Style ---` _(Rough.txt line 230; unverified)_
- **Patrol Along** — `Patrol Along: Target ___ Positions ___ Come Back --- Style ---` _(Rough.txt line 231; unverified)_
- **Create Monster** — `Create Monster: Position .XYZ Type ___ Team Sequency . 0  Chase Enemy ---tf Action Type ___ Path ___ (Target)` _(Rough.txt line 232; unverified)_

### ACTION — BEHAVIOUR TREE

- **Set Blackboard Value** — `Set Blackboard Value: Behaviour Tree ___  Key .please enter the content  Value ___` _(Rough.txt line 238; unverified)_
- **Get Blackboard Value** — `Get Blackboard Value: Behaviour Tree ___  Key .please enter the content  (Value)` _(Rough.txt line 239; unverified)_
- **Get Node Variable** — `Get Node Variable: Node ___ Key . Please enter the content (Value)` _(Rough.txt line 240; unverified)_

### ACTION — OTHER

- **Restore All Properties** — `Restore All Properties: Weapon Entity ___` _(Rough.txt line 246; unverified)_
- **Modify properties** — `Modify properties: Formulate-able entity ___ Type --- Properties --- Change Method .---+/× Value  . 0` _(Rough.txt line 247; unverified)_
- **Set basic properties** — `Set basic properties: Formulate-able entity ___ Type --- Properties --- Value . 0` _(Rough.txt line 248; unverified)_
- **Revert to original properties** — `Revert to original properties: Formulate-able entity ___ Type --- Properties ---` _(Rough.txt line 249; unverified)_
- **Set Player Voice Status** — `Set Player Voice Status: Target ___ Is Disabled ---tf` _(Rough.txt line 250; unverified)_
- **Set Player Quick Message Status** — `Set Player Quick Message Status: Target ___ Is Disabled ---tf` _(Rough.txt line 251; unverified)_
- **Get Chat Channel** — `.Get Chat Channel: Index ---` _(Rough.txt line 252; unverified)_
- **Get Current Chat Channel** — `.Get Current Chat Channel: Target ___` _(Rough.txt line 253; unverified)_
- **Join Chat Channel** — `Join Chat Channel: Target ___ Channel ___` _(Rough.txt line 254; unverified)_
- **Quit Chat Channel** — `Quit Chat Channel: Target ___` _(Rough.txt line 255; unverified)_
- **Upload Game Result** — `Upload Game Result: Target ___ Result ___ Score Name ___ Score ___` _(Rough.txt line 256; unverified)_
- **So moving to the next Category 3.GAME so it has 12 Sub Categories and those are** — `So moving to the next Category 3.GAME so it has 12 Sub Categories and those are :` _(Rough.txt line 260; unverified)_

### GAME — GLOBAL

- **Pause Fixed Update** — `Pause Fixed Update` _(Rough.txt line 277; unverified)_
- **Resume Fixed Update** — `Resume Fixed Update` _(Rough.txt line 278; unverified)_
- **Enable Safe Zone** — `Enable Safe Zone: Center .XYZ Radius . 0  Wait Time (s) . 0  Duration (s) . 0  Damage . 0` _(Rough.txt line 279; unverified)_
- **Disable Safe Zone** — `Disable Safe Zone` _(Rough.txt line 280; unverified)_
- **Enable Moving Zone** — `Enable Moving Zone: Start Position .XYZ Target Position .XYZ Initial Radius .0 Final Radius .0 Duration (s) . 0  Damage . 0` _(Rough.txt line 281; unverified)_
- **Get Server Timestamp** — `.Get Server Timestamp` _(Rough.txt line 282; unverified)_
- **Get Server Timestamp (ms)** — `.Get Server Timestamp (ms)` _(Rough.txt line 283; unverified)_

### GAME — PLAYER

- **Add HP** — `Add HP: Target ___ Value .0` _(Rough.txt line 287; unverified)_
- **Teleport** — `Teleport: Target ___ Position .xyz Rotation .xyz` _(Rough.txt line 288; unverified)_
- **Gey Owner** — `.Gey Owner: Target ___` _(Rough.txt line 289; unverified)_
- **Set Behaviour Status** — `Set Behaviour Status: Target ___ Type --- Status ---` _(Rough.txt line 291; unverified)_
- **Set Forward** — `Set Forward: Target ___ Forward .XYZ` _(Rough.txt line 292; unverified)_
- **Get Skills** — `.Get Skills: Target ___` _(Rough.txt line 293; unverified)_
- **Set Skills** — `Set Skills: Target ___ Skills ___` _(Rough.txt line 294; unverified)_
- **Hit Fly** — `Hit Fly: Target ___ Direction .XYZ Duration (s) .0 Velocity Y . 0  Velocity XZ .  0  Change Rotation ---tf` _(Rough.txt line 295; unverified)_
- **Set Default UI Status** — `Set Default UI Status: Target ___ Type .--- Status .---close/show` _(Rough.txt line 296; unverified)_
- **Get Random Spawn Position** — `.Get Random Spawn Position: Target ___` _(Rough.txt line 297; unverified)_
- **Set Falling Damage** — `Set Falling Damage: Target ___ Height Segments ___ Damage Segments ___` _(Rough.txt line 298; unverified)_
- **Exit Vehicle** — `Exit Vehicle: Target ___` _(Rough.txt line 299; unverified)_
- **Revive At Next Frame** — `Revive At Next Frame: Target ___` _(Rough.txt line 300; unverified)_
- **Quit Game at Next Frame** — `Quit Game at Next Frame: Target ___` _(Rough.txt line 301; unverified)_

### GAME — TEAM

- **Set Attackable Team** — `Set Attackable Team: Attacker ___ Target ___ Attackable .---tf` _(Rough.txt line 305; unverified)_
- **Get Position Near Team** — `.Get Position Near Team: Target ___` _(Rough.txt line 306; unverified)_
- **Set Attackable Entity** — `Set Attackable Entity: Attacker ___ Target ___ Attackable .---tf` _(Rough.txt line 307; unverified)_
- **Get Position Near Entity** — `.Get Position Near Entity: Attacker ___` _(Rough.txt line 308; unverified)_
- **Join Team** — `Join Team: Target ___  Target Team ___ (Status Code)` _(Rough.txt line 309; unverified)_
- **Join New Team** — `Join New Team: Target ___ (New Team, Status Code)` _(Rough.txt line 310; unverified)_
- **Eliminate At Next Frame** — `Eliminate At Next Frame: Target ___` _(Rough.txt line 311; unverified)_

### GAME — PHYSICS

- **Is Inside Sphere** — `.Is Inside Sphere: Target ___ Center .XYZ Radius . 0` _(Rough.txt line 317; unverified)_
- **Is Inside Cylinder** — `.Is Inside Cylinder: Target ___ Center .XYZ Radius . 0  Height . 0  Rotation.xyz` _(Rough.txt line 318; unverified)_
- **Is Inside Box** — `.Is Inside Box: Target ___ Center .XYZ Length . 0 Width . 0  Height . 0  Rotation.xyz` _(Rough.txt line 319; unverified)_
- **Is Inside Cylinder** — `.Is Inside Cylinder: Target ___ Center .XYZ Radius . 0 Cut Radius . 0  Height . 0  Angle . 0  Rotation.xyz` _(Rough.txt line 320; unverified)_
- **Single Raycast** — `Single Raycast: Start Position .XYZ Direction .XYZ Distance . 0  Layer Mask ___ Include Trigger .---tf (Hit Entities, Hit Points, Hit Distance, Hit Normals)` _(Rough.txt line 321; unverified)_
- **Multi-Raycast** — `Multi-Raycast: Start Position .XYZ Direction .XYZ Distance . 0  Layer Mask ___ Include Trigger .---tf (Hit Entities, Hit Points, Hit Distance, Hit Normals)` _(Rough.txt line 322; unverified)_
- **Box Cast** — `Box Cast: Half Extents .XYZ Center .XYZ Rotating .XYZ Direction .XYZ Max. Distance .0 Layer Mask ___ Include Trigger .---tf (Hit Entities)` _(Rough.txt line 323; unverified)_
- **Sphere Cast** — `Sphere Cast: Radius .0 Center .XYZ Direction .XYZ Max Distance .0 Layer Mask ___ Include Trigger .---tf (Hit Entities)` _(Rough.txt line 324; unverified)_
- **Capsule Cast** — `Capsule Cast: Radius .0 Height .0 Center .XYZ Rotation .XYZ Direction .XYZ Max Distance .0 Layer Mask ___ Include Trigger .---tf (Hit Entities)` _(Rough.txt line 325; unverified)_
- **Box Overlap** — `Box Overlap: Half Extents .XYZ Center .XYZ Rotation .XYZ Layer Mask ___ Include Trigger .---tf (Hit Entities)` _(Rough.txt line 326; unverified)_
- **Sphere Overlap** — `Sphere Overlap: Radius .0 Center .XYZ Layer Mask ___ Include Trigger.---tf (Hit Entities)` _(Rough.txt line 327; unverified)_
- **Capsule Overlap** — `Capsule Overlap: Radius .0 Height .0 Center .XYZ Rotation .XYZ Layer Mask ___ Include Trigger ___ (Hit Entities)` _(Rough.txt line 328; unverified)_

### GAME — CAMERA

- **Get Current Custom Camera** — `.Get Current Custom Camera: Target ___` _(Rough.txt line 334; unverified)_
- **Switch Custom Camera** — `Switch Custom Camera: Player ___ Camera ___ Transition Type --- Transition Time (ms) .0` _(Rough.txt line 335; unverified)_
- **Create Custom Camera (Created Entity)** — `Create Custom Camera (Created Entity)` _(Rough.txt line 336; unverified)_

### GAME — WORK FLOW

- **Switch Phase** — `Switch Phase: Phase Index .0` _(Rough.txt line 340; unverified)_
- **End Current Phase** — `End Current Phase` _(Rough.txt line 341; unverified)_

### GAME — ECONOMY

- **Get Wallet** — `Get Wallet: Target ___ (IsExist, Wallet)` _(Rough.txt line 345; unverified)_
- **Create Wallet** — `Create Wallet: Owner ___ Target ___ (Created Entity)` _(Rough.txt line 346; unverified)_
- **Add Money** — `Add Money: Target ___ Money Type --- Count .0` _(Rough.txt line 347; unverified)_
- **Cost Money** — `Cost Money: Target ___ Money Type --- Count .0` _(Rough.txt line 348; unverified)_
- **Transfer Money** — `Transfer Money: Out Wallet ___ Money Type --- Count .0 In Wallet ___` _(Rough.txt line 349; unverified)_
- **Get Money Count** — `.Get Money Count: Target ___ Money Type ---` _(Rough.txt line 350; unverified)_
- **Get Money** — `.Get Money: Target ___ Money Type ---` _(Rough.txt line 351; unverified)_
- **Get All Shops** — `.Get All Shops` _(Rough.txt line 352; unverified)_
- **Create Shop** — `Create Shop: (Created Entity)` _(Rough.txt line 353; unverified)_
- **Create Shop Shelf** — `Create Shop Shelf: (Created Entity)` _(Rough.txt line 354; unverified)_
- **Create Shop Item** — `Create Shop Item: (Created Entity)` _(Rough.txt line 355; unverified)_
- **Add Item To Shop Item** — `Add Item To Shop Item: Shop Item ___ Item ___ Count .0` _(Rough.txt line 356; unverified)_

### GAME — MINIMAP

- **Create Mini Map Icon** — `Create Mini Map Icon: Target ___ Resource --- (Created Entity)` _(Rough.txt line 362; unverified)_
- **Create Mini Map Pixel** — `Create Mini Map Pixel: Target ___ Bound Target ___ (Created Entity)` _(Rough.txt line 363; unverified)_

### GAME — ANIMATION

- **Play Animation** — `Play Animation: Target ___ State .'please enter the content' Play Speed .0 Loop Type ---` _(Rough.txt line 368; unverified)_
- **Stop Animation** — `Stop Animation: Target ___ State .'please enter the content'` _(Rough.txt line 369; unverified)_
- **Set Body Part Weight** — `Set Body Part Weight: Target ___ Body Part Name .' please enter the content' Weight .0` _(Rough.txt line 370; unverified)_

### GAME — COLLECTION

- **Play Emote** — `Play Emote: Target ___ Emote .---` _(Rough.txt line 376; unverified)_
- **Pause Emote** — `Pause Emote: Target ___ Is Pause .---tf` _(Rough.txt line 377; unverified)_
- **Get Outfit** — `.Get Outfit: Target ___ Type ___` _(Rough.txt line 378; unverified)_
- **Set Outfit** — `Set Outfit: Target ___ Outfit ___` _(Rough.txt line 379; unverified)_
- **Reset Outfit** — `Reset Outfit  Target ___` _(Rough.txt line 380; unverified)_
- **Remove Outfit** — `Remove Outfit: Target ___ Type ___` _(Rough.txt line 381; unverified)_
- **Get Weapon Skin** — `.Get Weapon Skin: Target ___ Weapon .---` _(Rough.txt line 382; unverified)_
- **Set Weapon Skin** — `Set Weapon Skin: Target ___ Weapon Skin ___` _(Rough.txt line 383; unverified)_
- **Reset Weapon Skin** — `Reset Weapon Skin: Target ___ Weapon .---` _(Rough.txt line 384; unverified)_
- **Remove Weapon Skin** — `Remove Weapon Skin: Target ___ Weapon .---` _(Rough.txt line 385; unverified)_
- **Get Vehicle Skin** — `.Get Vehicle Skin: Target ___ Vehicle ___` _(Rough.txt line 386; unverified)_
- **Set Vehicle Skin** — `Set Vehicle Skin: Target ___ Vehicle Skin .---` _(Rough.txt line 387; unverified)_
- **Reset Vehicle Skin** — `Reset Vehicle Skin: Target ___ Vehicle ___` _(Rough.txt line 388; unverified)_
- **Remove Vehicle Skin** — `Remove Vehicle Skin: Target ___ Vehicle ___` _(Rough.txt line 389; unverified)_
- **Get Backpack Skin** — `.Get Backpack Skin: Target ___` _(Rough.txt line 390; unverified)_
- **Set Backpack Skin** — `Set Backpack Skin: Target ___ Backpack Skin .---` _(Rough.txt line 391; unverified)_
- **Reset Backpack Skin** — `Reset Backpack Skin: Target ___` _(Rough.txt line 392; unverified)_
- **Remove Backpack Skin** — `Remove Backpack Skin: Target ___` _(Rough.txt line 393; unverified)_

### GAME — STORY

- **Notify Start Plot** — `Notify Start Plot: Target ___ Plot ID ___` _(Rough.txt line 399; unverified)_

### GAME — OTHER

- **End Morph** — `End Morph: Player ___` _(Rough.txt line 406; unverified)_
- **Morph To** — `Morph To: Player ___ Target ___ ( Created Entity)` _(Rough.txt line 407; unverified)_
- **Copy To Morph** — `Copy To Morph: Player ___ Target ___ ( Created Entity)` _(Rough.txt line 408; unverified)_
- **Get Morph** — `.Get Morph` _(Rough.txt line 409; unverified)_
- **Add Football Velocity** — `Add Football Velocity: Foot Ball ___ Velocity .XYZ` _(Rough.txt line 410; unverified)_
- **Set Football Position** — `Set Football Position: Football ___ Velocity .XYZ` _(Rough.txt line 411; unverified)_
- **Set Jersey** — `Set Jersey: Target ___ Jersey Type .--- Main Color1 ___ Main Color2 ___ Other Color ___` _(Rough.txt line 412; unverified)_
- **Reset Jersey** — `Reset Jersey: Player ___` _(Rough.txt line 413; unverified)_
- **Set Distance Volumes** — `Set Distance Volumes: Distance List ___ Volume List ___ (Created Entity)` _(Rough.txt line 414; unverified)_

### DATA — BASIC

- **Number = .0** — `Number = .0` _(Rough.txt line 435; unverified)_
- **String = . 'Please enter the content'** — `String = . 'Please enter the content'` _(Rough.txt line 436; unverified)_
- **Vector3 = .X0 Y0 Z0** — `Vector3 = .X0 Y0 Z0` _(Rough.txt line 437; unverified)_
- **List = .Empty list** — `List = .Empty list` _(Rough.txt line 438; unverified)_
- **Bool = .---tf** — `Bool = .---tf` _(Rough.txt line 439; unverified)_
- **Color = .Color⬜ (we can choose any colour from pallet or grid there)** — `Color = .Color⬜ (we can choose any colour from pallet or grid there)` _(Rough.txt line 440; unverified)_
- **entity = .No entity (you're aware of this block ig, i mentioned it before)** — `entity = .No entity (you're aware of this block ig, i mentioned it before)` _(Rough.txt line 441; unverified)_
- **NULL** — `.NULL` _(Rough.txt line 442; unverified)_
- **Curve Custom (here in the custom if we click we can create curve yk)** — `.Curve Custom (here in the custom if we click we can create curve yk)` _(Rough.txt line 443; unverified)_

### DATA — MATH

- **___ ---___➕** — `.___ ---___➕ (in this component that drop down has +-*/% and clicking that ➕ icon will add another slot and a drop down yk, it's like we can add multiple slots like this ___---___---___---___)` _(Rough.txt line 451; unverified)_
- **Random Int** — `.Random Int: Min .0 Max .0` _(Rough.txt line 452; unverified)_
- **Random Float** — `.Random Float: Min .0 Max .0` _(Rough.txt line 453; unverified)_
- **Abs** — `.Abs: Value .0` _(Rough.txt line 454; unverified)_
- **Sqrt** — `.Sqrt: Value .0` _(Rough.txt line 455; unverified)_
- **Negate** — `.Negate: Value .0` _(Rough.txt line 456; unverified)_
- **Vector addition** — `.Vector addition: ValueA .XYZ ValueB .XYZ` _(Rough.txt line 457; unverified)_
- **Vector substraction** — `.Vector substraction: ValueA .XYZ ValueB .XYZ` _(Rough.txt line 458; unverified)_
- **Vector multiplication** — `.Vector multiplication: Value .XYZ Scale .0` _(Rough.txt line 459; unverified)_
- **Dot** — `.Dot: ValueA .XYZ ValueB .XYZ` _(Rough.txt line 460; unverified)_
- **Cross** — `.Cross: ValueA .XYZ ValueB .XYZ` _(Rough.txt line 461; unverified)_
- **Distance** — `.Distance: ValueA .XYZ ValueB .XYZ` _(Rough.txt line 462; unverified)_
- **Angle** — `.Angle: ValueA .XYZ ValueB .XYZ` _(Rough.txt line 463; unverified)_
- **Projection** — `.Projection: ValueA .XYZ ValueB .XYZ` _(Rough.txt line 464; unverified)_
- **Lerp Vector3** — `.Lerp Vector3: ValueA .XYZ ValueB .XYZ ValueT .0` _(Rough.txt line 465; unverified)_
- **Slerp Vector3** — `.Slerp Vector3: ValueA .XYZ ValueB .XYZ ValueT .0` _(Rough.txt line 466; unverified)_
- **Magnitude** — `.Magnitude: Value .XYZ` _(Rough.txt line 467; unverified)_
- **Normalize** — `.Normalize: Value .XYZ` _(Rough.txt line 468; unverified)_
- **Vector2** — `.Vector2: Scale 2D Vector ___ Scale .0` _(Rough.txt line 469; unverified)_
- **Vector2** — `.Vector2: Add ValueA ___ ValueB ___` _(Rough.txt line 470; unverified)_
- **Vector2 Sub** — `.Vector2 Sub: ValueA ___ ValueB ___` _(Rough.txt line 471; unverified)_
- **Vector2Dot** — `.Vector2Dot: ValueA ___ ValueB ___` _(Rough.txt line 472; unverified)_
- **Vector2Distance** — `.Vector2Distance: ValueA ___ ValueB ___` _(Rough.txt line 473; unverified)_
- **Vector2Angle** — `.Vector2Angle: ValueA ___ ValueB ___` _(Rough.txt line 474; unverified)_
- **Vector2Normalize** — `.Vector2Normalize: Value ___` _(Rough.txt line 475; unverified)_
- **Vector2Magnitude** — `.Vector2Magnitude: Value ___` _(Rough.txt line 476; unverified)_
- **Vector2Reflect** — `.Vector2Reflect: Direction .XYZ Normal .XYZ` _(Rough.txt line 477; unverified)_
- **Vector2Reflect** — `.Vector2Reflect: Direction ___ Normal ___` _(Rough.txt line 478; unverified)_
- **Rotate Vector** — `.Rotate Vector: Value .XYZ Delta ___` _(Rough.txt line 479; unverified)_
- **Max** — `.Max: ValueA .0 ValueB .0` _(Rough.txt line 480; unverified)_
- **Min** — `.Min: ValueA .0 ValueB .0` _(Rough.txt line 481; unverified)_
- **Lerp** — `.Lerp: ValueA .0 ValueB .0 ValueT .0` _(Rough.txt line 482; unverified)_
- **Clamp** — `.Clamp: Value .0 Min .0 Max .0` _(Rough.txt line 483; unverified)_
- **Exponentiation** — `.Exponentiation: Base .0 Exponent .0` _(Rough.txt line 484; unverified)_
- **Logarithm** — `.Logarithm: Base .0 Real Number .0` _(Rough.txt line 485; unverified)_
- **Ceil** — `.Ceil: Value  .0` _(Rough.txt line 486; unverified)_
- **Floor** — `.Floor: Value  .0` _(Rough.txt line 487; unverified)_
- **Round** — `.Round: Value  .0` _(Rough.txt line 488; unverified)_
- **ASin** — `.ASin: Value  .0` _(Rough.txt line 489; unverified)_
- **ACos** — `.ACos: Value  .0` _(Rough.txt line 490; unverified)_
- **Sin** — `.Sin: Degree .0` _(Rough.txt line 491; unverified)_
- **Cos** — `.Cos: Degree .0` _(Rough.txt line 492; unverified)_
- **Tan** — `.Tan: Degree .0` _(Rough.txt line 493; unverified)_
- **Value** — `.Value: Degree .0` _(Rough.txt line 494; unverified)_
- **ATan2** — `.ATan2: Y .0 X .0` _(Rough.txt line 495; unverified)_
- **Quaternion Angle** — `.Quaternion Angle: Left Value ___ Right Value ___` _(Rough.txt line 496; unverified)_
- **Quaternion Dot** — `.Quaternion Dot: Left Value ___ Right Value ___` _(Rough.txt line 497; unverified)_
- **Quaternion Inverse** — `.Quaternion Inverse: Value ___` _(Rough.txt line 498; unverified)_
- **Quaternion From To Rotation** — `.Quaternion From To Rotation: From .XYZ To .XYZ` _(Rough.txt line 499; unverified)_
- **Quaternion Rotate Toward** — `.Quaternion Rotate Toward: From ___ To ___ Max Degree Delta .0` _(Rough.txt line 500; unverified)_

### DATA — LIST

- **Append** — `Append: Target ___ Value ___` _(Rough.txt line 508; unverified)_
- **Remove** — `Remove: Target ___ Value ___` _(Rough.txt line 509; unverified)_
- **Contain** — `.Contain: Target ___ Value ___` _(Rough.txt line 510; unverified)_
- **Modify** — `Modify: List ___ Index .0 Value ___` _(Rough.txt line 511; unverified)_
- **Obtain** — `.Obtain: List ___ Index .0` _(Rough.txt line 512; unverified)_
- **Length** — `.Length: Target ___` _(Rough.txt line 513; unverified)_
- **Remove At** — `Remove At: Target ___ Index .0` _(Rough.txt line 514; unverified)_
- **Append Range** — `Append Range: Target ___ Value ___` _(Rough.txt line 515; unverified)_
- **Index Of** — `.Index Of: Target ___ Value ___` _(Rough.txt line 516; unverified)_
- **Last Index Of** — `.Last Index Of: Target ___ Value ___` _(Rough.txt line 517; unverified)_
- **Clear** — `Clear: Target ___` _(Rough.txt line 518; unverified)_
- **Reverse** — `Reverse: Target ___` _(Rough.txt line 519; unverified)_
- **Clone** — `.Clone: Target ___` _(Rough.txt line 520; unverified)_
- **Insert** — `Insert: Target ___ Index .0 Value ___` _(Rough.txt line 521; unverified)_
- **Shuffle** — `Shuffle: Target ___` _(Rough.txt line 522; unverified)_
- **Is Equal** — `.Is Equal: Left Value ___ Right Value ___` _(Rough.txt line 523; unverified)_
- **Max** — `Max: Target ___ (Is Success, Result)` _(Rough.txt line 524; unverified)_
- **Min** — `Min: Target ___ (Is Success, Result)` _(Rough.txt line 525; unverified)_

### DATA — DICTIONARY

- **Create Random Seed** — `.Create Random Seed: Seed .0` _(Rough.txt line 533; unverified)_
- **Next** — `.Next: Value .0 Min .0 Max .0` _(Rough.txt line 534; unverified)_

### DATA — VECTOR

- **Get vector** — `.Get vector: X .0  Y .0  Z .0` _(Rough.txt line 540; unverified)_
- **Get x vector vomponent** — `.Get x vector vomponent: Vector .XYZ` _(Rough.txt line 541; unverified)_
- **Get y vector component** — `.Get y vector component: Vector .XYZ` _(Rough.txt line 542; unverified)_
- **Obtain z vector component** — `.Obtain z vector component: Vector .XYZ` _(Rough.txt line 543; unverified)_
- **Set x vector component** — `Set x vector component: Vector .XYZ X .0` _(Rough.txt line 544; unverified)_
- **Set y vector component** — `Set y vector component: Vector .XYZ Y .0` _(Rough.txt line 545; unverified)_
- **Set z vector component** — `Set z vector component: Vector .XYZ Z .0` _(Rough.txt line 546; unverified)_
- **New Vector2** — `New Vector2: X .0 Y .0` _(Rough.txt line 547; unverified)_
- **Vector2 Get X** — `.Vector2 Get X: 2D Vector ___` _(Rough.txt line 548; unverified)_
- **Vector2 Get Y** — `.Vector2 Get Y: 2D Vector ___` _(Rough.txt line 549; unverified)_
- **Vector2 Set X** — `Vector2 Set X: 2D Vector ___ X .0` _(Rough.txt line 550; unverified)_
- **Vector2 Set Y** — `Vector2 Set Y: 2D Vector ___ Y .0` _(Rough.txt line 551; unverified)_

### DATA — STRINGS

- **Connect** — `.Connect: Value1 ___ Value2 ___ ➕(i already explained what this sign ➕ means)` _(Rough.txt line 557; unverified)_
- **Length** — `.Length: Value .text` _(Rough.txt line 558; unverified)_
- **Replace** — `.Replace: Target .text Old Value .text New Value .text` _(Rough.txt line 559; unverified)_
- **Find** — `.Find: Target .text Find Value .text Start Index .0` _(Rough.txt line 560; unverified)_
- **Sub** — `.Sub: Target .text Start Index .0 Length .0` _(Rough.txt line 561; unverified)_
- **Find At** — `.Find At: Target .text Indexs ___` _(Rough.txt line 562; unverified)_
- **Split** — `.Split: Target .text Separator .text` _(Rough.txt line 563; unverified)_
- **Join** — `.Join: Target ___ Sep .text` _(Rough.txt line 564; unverified)_
- **To Upper** — `.To Upper: Target .text` _(Rough.txt line 565; unverified)_
- **To Lower** — `.To Lower: Target .text` _(Rough.txt line 566; unverified)_
- **Strip** — `.Strip: Target .text` _(Rough.txt line 567; unverified)_
- **Format String** — `.Format String: Content .text Parameters Array ___` _(Rough.txt line 568; unverified)_

### DATA — CONVERT

- **To String** — `.To String: Target ___` _(Rough.txt line 574; unverified)_
- **String To Int** — `String To Int: Target .text (Result, Is Success)` _(Rough.txt line 575; unverified)_
- **String To Float** — `String To Float: Target .text (Result, Is Success)` _(Rough.txt line 576; unverified)_
- **Int To Float** — `.Int To Float: Value .0` _(Rough.txt line 577; unverified)_
- **Vector3 To Vector2** — `.Vector3 To Vector2: Target .XYZ` _(Rough.txt line 578; unverified)_
- **Vector2 To Vector3** — `.Vector2 To Vector3: Target___` _(Rough.txt line 579; unverified)_
- **Euler Angle to Vector3** — `.Euler Angle to Vector3: Value .XYZ` _(Rough.txt line 580; unverified)_
- **Direction to Euler Angle** — `.Direction to Euler Angle: Direction .XYZ` _(Rough.txt line 581; unverified)_
- **Timestamp to Localized String (ms)** — `.Timestamp to Localized String (ms): Timestamp (ms) ___ Style .---` _(Rough.txt line 582; unverified)_
- **Bitwise List to Int** — `.Bitwise List to Int: Bit Array ___` _(Rough.txt line 583; unverified)_
- **Bitwise Int to List** — `.Bitwise Int to List: Value .0` _(Rough.txt line 584; unverified)_

### DATA — ENUM

- **Damage Type** — `1. Damage Type .---` _(Rough.txt line 589; unverified)_
- **Score Type** — `2. Score Type .---` _(Rough.txt line 590; unverified)_
- **Built-in UI Type (I'm not writting.--- because it's time consuming so don't get confused, yk what maybe I don't need to type them as I already told u up there hehe)** — `3. Built-in UI Type (I'm not writting.--- because it's time consuming so don't get confused, yk what maybe I don't need to type them as I already told u up there hehe)` _(Rough.txt line 591; unverified)_
- **Icon Type** — `4. Icon Type` _(Rough.txt line 592; unverified)_
- **VFX Type** — `5. VFX Type` _(Rough.txt line 593; unverified)_
- **Sound Effect Type** — `6. Sound Effect Type` _(Rough.txt line 594; unverified)_
- **Item ID Type** — `7. Item ID Type` _(Rough.txt line 595; unverified)_
- **Dynamic Create Level Object Type** — `8. Dynamic Create Level Object Type` _(Rough.txt line 596; unverified)_
- **Property Modify Type** — `9. Property Modify Type` _(Rough.txt line 597; unverified)_
- **Inventory Type** — `10. Inventory Type` _(Rough.txt line 598; unverified)_
- **Type Enum** — `11. Type Enum` _(Rough.txt line 599; unverified)_
- **Patrol Style Type** — `12. Patrol Style Type` _(Rough.txt line 600; unverified)_
- **Patrol Type** — `13. Patrol Type` _(Rough.txt line 601; unverified)_
- **Money Type** — `14. Money Type` _(Rough.txt line 602; unverified)_
- **SkyboxType** — `15. SkyboxType` _(Rough.txt line 603; unverified)_
- **Player Revival Source Type** — `16. Player Revival Source Type` _(Rough.txt line 604; unverified)_
- **Equipment Type** — `17. Equipment Type` _(Rough.txt line 605; unverified)_
- **Aim Assist Type** — `18. Aim Assist Type` _(Rough.txt line 606; unverified)_
- **Player Behaviour Status Type** — `19. Player Behaviour Status Type` _(Rough.txt line 607; unverified)_
- **Buff Type** — `20. Buff Type` _(Rough.txt line 608; unverified)_
- **Loot Weapon Type** — `21. Loot Weapon Type` _(Rough.txt line 609; unverified)_
- **Object Texture** — `22. Object Texture` _(Rough.txt line 610; unverified)_
- **Monster Type** — `23. Monster Type` _(Rough.txt line 611; unverified)_
- **Effect Texture Type** — `24. Effect Texture Type` _(Rough.txt line 612; unverified)_
- **Loot Armor Type** — `25. Loot Armor Type` _(Rough.txt line 613; unverified)_
- **Loot Ammo Type** — `26. Loot Ammo Type` _(Rough.txt line 614; unverified)_
- **Loot Consumable Type** — `27. Loot Consumable Type` _(Rough.txt line 615; unverified)_
- **Loot Throwable Type** — `28. Loot Throwable Type` _(Rough.txt line 616; unverified)_
- **Loot Scope Type** — `29. Loot Scope Type` _(Rough.txt line 617; unverified)_
- **Movable Platform Type** — `30. Movable Platform Type` _(Rough.txt line 618; unverified)_
- **Tween Style Type** — `31. Tween Style Type` _(Rough.txt line 619; unverified)_
- **Coordinate System Type** — `32. Coordinate System Type` _(Rough.txt line 620; unverified)_
- **Mini Sentry Attack Range Type** — `33. Mini Sentry Attack Range Type` _(Rough.txt line 621; unverified)_
- **Loot Scorer Type** — `34. Loot Scorer Type` _(Rough.txt line 622; unverified)_
- **Character skill** — `35. Character skill` _(Rough.txt line 623; unverified)_
- **Outfit Slot Type** — `36. Outfit Slot Type` _(Rough.txt line 624; unverified)_
- **Player UI Type** — `37. Player UI Type` _(Rough.txt line 625; unverified)_
- **Switch Equip Slot** — `38. Switch Equip Slot` _(Rough.txt line 626; unverified)_
- **3-Status Switch** — `39. 3-Status Switch` _(Rough.txt line 627; unverified)_
- **Gender Type** — `40. Gender Type` _(Rough.txt line 628; unverified)_
- **Special ID Type** — `41. Special ID Type` _(Rough.txt line 629; unverified)_
- **Equipment Slot Type** — `42. Equipment Slot Type` _(Rough.txt line 630; unverified)_
- **Damage Body Part Type** — `43. Damage Body Part Type` _(Rough.txt line 631; unverified)_
- **Fill Direction Type** — `44. Fill Direction Type` _(Rough.txt line 632; unverified)_
- **Fill Type** — `45. Fill Type` _(Rough.txt line 633; unverified)_
- **Seat Type** — `46. Seat Type` _(Rough.txt line 634; unverified)_
- **Font Type** — `47. Font Type` _(Rough.txt line 635; unverified)_
- **Player Pose Type** — `48. Player Pose Type` _(Rough.txt line 636; unverified)_
- **Knok-down Type** — `49. Knok-down Type` _(Rough.txt line 637; unverified)_
- **Action Type** — `50. Action Type` _(Rough.txt line 638; unverified)_
- **Fire Type** — `51. Fire Type` _(Rough.txt line 639; unverified)_
- **Layout Sort Type** — `52. Layout Sort Type` _(Rough.txt line 640; unverified)_
- **Status Code** — `53. Status Code` _(Rough.txt line 641; unverified)_
- **Camera Viewing Angle Restriction Type** — `54. Camera Viewing Angle Restriction Type` _(Rough.txt line 642; unverified)_
- **Weapon Skin Type** — `55. Weapon Skin Type` _(Rough.txt line 643; unverified)_
- **Backpack Skin Type** — `56. Backpack Skin Type` _(Rough.txt line 644; unverified)_
- **Fog Mode Type** — `57. Fog Mode Type` _(Rough.txt line 645; unverified)_
- **Rigidbody Constrain Type** — `58. Rigidbody Constrain Type` _(Rough.txt line 646; unverified)_
- **Phase And Round Enum** — `59. Phase And Round Enum` _(Rough.txt line 647; unverified)_
- **Force Type** — `60. Force Type` _(Rough.txt line 648; unverified)_
- **LoopType** — `61. LoopType` _(Rough.txt line 649; unverified)_
- **Render Quality Type** — `62. Render Quality Type` _(Rough.txt line 650; unverified)_
- **Player State Type** — `63. Player State Type` _(Rough.txt line 651; unverified)_
- **Vehicle Skin Type** — `64. Vehicle Skin Type` _(Rough.txt line 652; unverified)_
- **Outfit Skin Type** — `65. Outfit Skin Type` _(Rough.txt line 653; unverified)_

### LOGIC — CONTROL FLOW

- **'if else statement'** — `'if else statement'` _(Rough.txt line 660; unverified)_
- **'if statement'** — `'if statement'` _(Rough.txt line 662; unverified)_
- **Then we have 'conditional loop'** — `Then we have 'conditional loop'` _(Rough.txt line 664; unverified)_
- **then we have 'loop of integer range' which returns** — `then we have 'loop of integer range' which returns ( index name ) and then together we have 'Start Value .0 End Value .10 Step .1'` _(Rough.txt line 665; unverified)_
- **Then we have 'Loop every element'** — `Then we have 'Loop every element' (Index Name, Element) Data Container ___` _(Rough.txt line 666; unverified)_
- **Two more block in logic are Continue to next and Break Loop** — `Two more block in logic are Continue to next and Break Loop` _(Rough.txt line 667; unverified)_

### VAR — VARIABLE TYPES

_No candidate lines extracted automatically. Consult the raw source._

### FUNC — FUNCTIONS

_No candidate lines extracted automatically. Consult the raw source._

## Observed enum-like dropdown/type names

1. Damage Type
2. Score Type
3. Built-in UI Type
4. Icon Type
5. VFX Type
6. Sound Effect Type
7. Item ID Type
8. Dynamic Create Level Object Type
9. Property Modify Type
10. Inventory Type
11. Type Enum
12. Patrol Style Type
13. Patrol Type
14. Money Type
15. SkyboxType
16. Player Revival Source Type
17. Equipment Type
18. Aim Assist Type
19. Player Behaviour Status Type
20. Buff Type
21. Loot Weapon Type
22. Object Texture
23. Monster Type
24. Effect Texture Type
25. Loot Armor Type
26. Loot Ammo Type
27. Loot Consumable Type
28. Loot Throwable Type
29. Loot Scope Type
30. Movable Platform Type
31. Tween Style Type
32. Coordinate System Type
33. Mini Sentry Attack Range Type
34. Loot Scorer Type
35. Character skill
36. Outfit Slot Type
37. Player UI Type
38. Switch Equip Slot
39. 3-Status Switch
40. Gender Type
41. Special ID Type
42. Equipment Slot Type
43. Damage Body Part Type
44. Fill Direction Type
45. Fill Type
46. Seat Type
47. Font Type
48. Player Pose Type
49. Knok-down Type
50. Action Type
51. Fire Type
52. Layout Sort Type
53. Status Code
54. Camera Viewing Angle Restriction Type
55. Weapon Skin Type
56. Backpack Skin Type
57. Fog Mode Type
58. Rigidbody Constrain Type
59. Phase And Round Enum
60. Force Type
61. LoopType
62. Render Quality Type
63. Player State Type
64. Vehicle Skin Type
65. Outfit Skin Type

## Known review flags

- **Observed issue:** Several signatures contain likely spelling/transcription variants (for example 'Parnt', 'Gey Owner', 'LIAT', 'Knok-down').
  **Next action:** Keep literal source value; verify official name before normalizing.
- **Observed issue:** Two blocks are described as 'Is Inside Cylinder' with different parameter shapes.
  **Next action:** Check whether these are distinct block names or one mislabelled block.
- **Observed issue:** A few blocks have ambiguous labels or output descriptions, including the physics cast blocks, curve sampling, football positioning, property-formulation blocks, and enum dropdowns.
  **Next action:** Capture screenshots or query the installed editor/API reference before assigning semantic types.
- **Observed issue:** The rough notes describe the block editor, while the official docs also cover code scripts, .fcg/.fcc, client/server constraints, and PC/mobile differences.
  **Next action:** Keep visual block inventory separate from the PC code/API reference and explicitly link the shared concepts.
- **Observed issue:** The section headed 'DATA - DICTIONARY' lists Create Random Seed and Next, which look like random-seed utilities rather than dictionary operations.
  **Next action:** Verify the actual editor subcategory label and move/alias these entries only after the installed editor confirms their placement.
- **Observed issue:** Official enum reference marks Score Type, Character skill, and Effect Texture Type obsolete; all three appear in Rough.txt's enum-type list.
  **Next action:** Add obsolete status and official enum URLs to the verified layer. Do not recommend these entries for new work by default.
- **Observed issue:** Official block-script guide uses 'party scripts' for one default script scope, whereas Rough.txt says TEAM.
  **Next action:** Verify the target editor's exact label and runtime semantics; retain the user wording as an alias until confirmed.
- **Observed issue:** Official docs separate API, Event, Type, and Enum references and expose more modules than the rough seven-category list.
  **Next action:** Maintain both the user-facing visual-block taxonomy and an official-reference crosswalk rather than forcing a one-to-one mapping.

## Next verification pass

1. Compare observed block names against current official API/event/type/enum pages and editor search results.
2. Add structured fields to each verified item: canonical name, alias/transcription, input types, output types, server/client availability, Mobile/PC support, script context, version/deprecation, official URL, tested status.
3. Add enum values as separate records; the present list names enum dropdown types but does not enumerate every option inside each dropdown.
4. Request screenshots or exports only for cases where public docs do not expose the same block UI or option list.
5. Build example recipes only from verified signatures, and label compilation/playtest status separately.

Machine-readable counterpart: [`research/user-observed-block-inventory.json`](../research/user-observed-block-inventory.json).
