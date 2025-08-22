# --------- FRAMES NAV ---------
def select_frame_by_name(self, name):
    self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
    self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
    self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

    if name == "home":
        self.home_frame.grid(row=1, column=1, sticky="nsew")
    else:
        self.home_frame.grid_forget()
    if name == "frame_2":
        self.second_frame.grid(row=1, column=1, sticky="nsew")
    else:
        self.second_frame.grid_forget()
    if name == "frame_3":
        self.third_frame.grid(row=1, column=1, sticky="nsew")
    else:
        self.third_frame.grid_forget()