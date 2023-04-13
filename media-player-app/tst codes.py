kv_music = '''
<MusicWindow>:
    MDBoxLayout:
        orientation: "vertical"
        MDScrollView:
            bar_width: 0
            height: "680dp"
            do_scroll_y: True
            effect_cls: "ScrollEffect"
            MDBoxLayout:
                orientation: "vertical"

                NavBarTop:
                    size_hint_y: None
                    height: "40dp"

                MDTabs:
                    id: tabs
                    on_tab_switch: app.on_tab_switch(*args)
                    size_hint_y: None
                    height: "40dp"
                    tab_indicator_anim: False
                    background_color: 0.2, 0.2, 0.2, 1
                    tab_color: 1, 1, 1, 1

                    MDTabsBase:
                        text: "Tab 1"

                    MDTabsBase:
                        text: "Tab 2"

                    MDTabsBase:
                        text: "Tab 3"

                    MDTabsBase:
                        text: "Tab 4"

                NavBarBottom:
                    size_hint_y: None
                    height: "60dp"

<NavBarTop@NavBar>:
    radius: [14]
    elevation: 4
    size_hint: .95, None
    size_hint_x: "40dp"
    md_bg_color: 0, 0, 0, 0
    pos_hint: {"center_x": .5, "center_y": .07}

<NavBarBottom@NavBar>:
    elevation: 4
    size_hint: 1, None
    size_hint_x: "90%"
    md_bg_color: 0, 0, 0, 0
    radius: [0, 0, 30, 30]
    pos_hint: {"center_x": .5, "center_y": .07}
    MDGridLayout:
        cols: 5
        spacing: "17dp"
        pos_hint: {"center_x": .5, "center_y": .55}
        MDIconButton:
            id: nav_icon1
            icon: "home"
            ripple_scale: 3
            user_font_size: "50sp"
            theme_text_color: "Custom"
        MDIconButton:
            id: nav_icon1
            icon: "home"
            ripple_scale: 0
            user_font_size: "50sp"
            theme_text_color: "Custom"
        MDIconButton:
            id: nav_icon1
            icon: "home"
            ripple_scale: 0
            user_font_size: "70sp"
            theme_text_color: "Custom"
        MDIconButton:
            id: nav_icon1
            icon: "home"
            ripple_scale: 0
            user_font_size: "50sp"
            theme_text_color: "Custom"
        MDIconButton:
            id: nav_icon1
            icon: "home"
            ripple_scale: 0
            user_font_size: "50sp"
            theme_text_color: "Custom"

'''