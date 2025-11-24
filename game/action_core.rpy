init python:
    class Action:
        def __init__(self, name, time_cost=0, available_fn= lambda: True):
            self.name = name
            self.time_cost = time_cost
            self.available_fn = available_fn

        def is_available(self):
            return self.available_fn()

label after_action(next_location):
    # Add the time cost of the current action
    $ clock_hour += current_action.time_cost

    # Go back to the location flow
    jump expression next_location

################################################################################
## Action Screen
################################################################################

style action_button:
    background '#8F8476' 
    padding (10, 5)      
    hover_background '#c7ab87'
    insensitive_background '#3f3a35' 
    yalign 0.0 
    xoffset 120
    yoffset 10

screen action_menu(actions, prefix):
    style_prefix "choice"  # Use the same style as the choice screen

    fixed:

        ypos 0.12

        if len(actions) >= 6:
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"

                xsize gui.choice_button_width
                ysize config.screen_height - 600

                xalign 0.5
                yalign 0.3

                vbox:
                    for a in actions:
                        if a.is_available():
                            textbutton a.name:
                                action [
                                    Hide("action_menu"),
                                    SetVariable("current_action", a),
                                    Call(f"{prefix}_{clock_hour}h_{to_camel_case(a.name)}")
                                ]
                                at fade_in
        else:
            vbox:
                for a in actions:
                    if a.is_available():
                        textbutton a.name:
                            action [
                                    Hide("action_menu"),
                                    SetVariable("current_action", a),
                                    Call(f"{prefix}_{clock_hour}h_{to_camel_case(a.name)}")
                                ]
                            at fade_in

screen action():
    textbutton "ACTION":
        style "action_button"
        text_style "custom_button_text"
        sensitive not action_lock

        action If(
            'actions' in globals() and sum([x.is_available() for x in actions]) != 0,
            ToggleScreen(
                "action_menu",
                transition=dissolve_fast,
                actions=actions,
                prefix=prefix if 'prefix' in globals() else ""
            ),
            [Function(renpy.notify, "There is nothing for you to do.")]
        )