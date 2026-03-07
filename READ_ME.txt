## Drop_Off by Jim Gillispie (orginally by Andre Odendaal in Artemis 2.x)
## THIS IS MISSION VERSION: 1.2.8
##
## UPDATE HISTORY
## 1.0.0    initial release
##
## 1.0.1:   label indentation added, as per Doug's recommendation (I'm still not exactly sure why, but I'm just a novice coder, so I trust him!)
##          increased starting Kralien distance from stations (they were too close before, inducing early player panic)
##          increased time until the reminder message is sent after picking up commanders (i.e. space trucker CB vibe)
##          added the (necessary) "players" variable definintion in the two de-cloak labels, otherwise would cause MAST crash
##
## 1.0.2:   added some dense nebula regions and a big black hole (Gaia BH3) to make the sector a little more interesting
##          added support for multi-ship by checking to make sure which ship is carrying the commanders when docking
##          added ending checking for the case in which the player ship with the commanders is destroyed
##          sped up the ending_triggered label loop slightly
##          added a classic "big message" style intro message on main screen
##
## 1.0.2a:   added support for Cosmos v1.0.2.01
##          extended player sensors by adding a cheat: "spy asteroids", this will give more warning of Kraliens approaching
##          same as above, but with "nav asteroids" for nebula mapping
##          slightly increased the Kralien's starting distance from stations (again), now the Kraliens will destroy either DS-99 or DS-101 within 15-16 minutes without intervention (this should be perfect timing, creating a total of 25-30 minutes for a successful mission play-through)
##          added nav points for drop off stations, and also for Gaia BH3
##          made sure de-cloaking of Skaraans only occurs once the commanders have been picked up (story works better this way)
##          fixed comms messages that were originally assigned to the incorrect stations
##          slightly sooner de-cloak around DS-106, since these are the only enemies likely to threaten this station
##
## 1.0.6:   updated to work with Cosmos v1.0.6 release on Steam/Itch.io (FYI: that version uses the v1.0.4 SBS MAST libraries)
##          added friendly TSN ships that are commandable by Comms, the number of ships selectable by the "Friendly Ships" drop-down box
##          better checking for end-of-mission situations
##          EVEN SOONER de-cloak around DS-106
##          included a modified preferences.json for increased 2D and 3D render distances (needs to be copied manually two folders up over exisiting preferences.json on the server and all clients)
##          added enemy comms messages (to deepen the main story)
##          added an accretion disc and custom scan info to Gaia BH3 (world-building)
##          added voice-acting audio files for Admiral Akana, base Comms officers, and the Skaraans
##          included voice-acting credits in "big message"
##
## 1.1.3    updated to work with Cosmos .exe version 1.1.3 and SBS/MAST libraires version 1.1.0
##          switched friendly eyes to use the link() function
##          removed the navigation asteroids, I think there were too many friendly eyes?! But I kept the spy asteroids to spot the Kraliens.
##          assigned static faces to the bases and talking Skaraans
##          changed the creation of friendly TSN ships to use prefab_npc_defender() for better default AI
##          Admiral Akana is now a lifeform on SB-8, rather than the face of the station
##          added the commanders as lifeforms that move between stations and the player ship
##          added mine defenses for the base when lethal terrain is selected, moved NPC ships to avoid said mines
##          main screen visuals for voice-acted characters
##          added Quindar-like tones to the voice acting files, to make people pay more attention
##          more naturally shaped nebulas. Also turned off selectablilty for nebulas to make traversing nebulas simpler.
##          Comms can now question the Commanders during the mission
##          created periodic waterfall status readings on the location of the Commanders
##
## 1.1.6    updated to work with Cosmos .exe version 1.1.6
##          mission logo now appears briefly on the Main Screen at start
##          arguably the actual difficulty scales slower at DIFFICULTY 6+, so I added some extra Kralien fleets at DIFFICULTYs 6, 8, and 10
##          forced asteroids to be selectable (cuz they are fun to shoot!)
##          tweaked Gaia the black hole's accrection disc and gravity distance
##          increased default scanning and zoom range for asteroids/nebulas in the custom preferences.json (needs to be copied over the file 2 folders up)
##          unique roles were causing unwanted tabs for Science/Comms, so I switched to another method to select individual ships from fleets
##          Skaraan attacks are now triggered by distance check from stations, rather than entering a rectanglular area
##
## 1.2.1    updated to work with Cosmos .exe version 1.2.1
##          I changed the icon that appears on the server, but I may yet change it again in the future...
##          again optimized the preferences.json(needs to be copied over the file 2 folders up) for best mission playablity
##
## 1.2.3    updated to work with Cosmos .exe version 1.2.3 (using MAST libraries 1.3.0)
##          changed the versioning numbers (both historically and going forward) to be more aligned with Thom's Cosmos release versioning
##          delayed the victory for a extra 5 seconds to give time to read any comms messages
##
## 1.2.5    updated to work with Cosmos .exe version 1.2.5 (using MAST libraries 1.3.0)
##          more Skaraans will appear at higher difficulties
##          made reminder message from Akana appear slightly sooner
##
## 1.2.8    updated to work with Cosmos .exe version 1.2.8 (using MAST libraries 1.3.0)
##          using new version of settings.yaml from Legendary, but tweaked for Drop_Off
##          had to include new relationships/sides setup
##          tweaked Gaea's accretion disc color
##          fixed missing Comms Badge problem
##
## Future:  update nebulae to use new functions? Or upgrade old functions to use Warp slowing?
##          ability for Skaraans to detect where the commanders are?
##          reminder about tricksy Skaraan tech? 
##          allow players to surrender Cmdr Thompson to Skaraan justice? (e.g. jettison him into an "escape pod", i.e. shuttle?) Maybe Cmdr Richards too? A moral dilemma? What would Picard do? Then just auto-fail the mission.
##          Comms "Receiving Hail" button for voiced dialog? Replayablity of messages warrented?
##          further tweak Gaia the black hole's accrection disc, distance, density, gravity, etc. for maximum realism
##          fix PNG image stretching at certain resolutions
##          find a way to get blue nebulas with the new functions (test functions in tile.py still work, but are dated)
##          fix missing Comms Badge on stations with lifeforms
