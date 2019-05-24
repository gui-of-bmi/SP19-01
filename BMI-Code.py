if self.comboBox.currentIndex():
                if str(age_tt) <= str(20):
                        self.Ideal_Weight.setText(str("40 Kg. to 50 Kg."))
                        self.Ideal_Height.setText(str("4.0 ft to 5.5 ft"))
                elif str(age_tt) <= str(30):
                        self.Ideal_Weight.setText(str("50 Kg. to 60 Kg."))
                        self.Ideal_Height.setText(str("5.5 ft to 5.9 ft"))
                elif str(age_tt) <= str(40):
                        self.Ideal_Weight.setText(str("60 Kg. to 65 Kg."))
                        self.Ideal_Height.setText(str("5.5 ft to 5.9 ft"))
                elif str(age_tt) <= str(50):
                        self.Ideal_Weight.setText(str("65 Kg. to 68 Kg."))
                        self.Ideal_Height.setText(str("5.5 ft to 5.9 ft"))
                elif str(age_tt) <= str(60):
                        self.Ideal_Weight.setText(str("68 Kg. to 71 Kg."))
                        self.Ideal_Height.setText(str("5.5 ft to 5.9 ft"))
                elif str(age_tt) <= str(70):
                        self.Ideal_Weight.setText(str("65 Kg. to 68 Kg."))
                        self.Ideal_Height.setText(str("5.5 ft to 5.9 ft"))
        else:
                if str(age_tt) <= str(20):
                        self.Ideal_Weight.setText(str("45 Kg. to 58 Kg."))
                        self.Ideal_Height.setText(str("4.9 ft to 5.5 ft"))
                elif str(age_tt) <= str(30):
                        self.Ideal_Weight.setText(str("59 Kg. to 70 Kg."))
                        self.Ideal_Height.setText(str("5.0 ft to 6.0 ft"))
                elif str(age_tt) <= str(40):
                        self.Ideal_Weight.setText(str("70 Kg. to 73 Kg."))
                        self.Ideal_Height.setText(str("5.0 ft to 6.0 ft"))
                elif str(age_tt) <= str(50):
                        self.Ideal_Weight.setText(str("73 Kg. to 75 Kg."))
                        self.Ideal_Height.setText(str("5.0 ft to 6.0 ft"))
                elif str(age_tt) <= str(60):
                        self.Ideal_Weight.setText(str("75 Kg. to 77 Kg."))
                        self.Ideal_Height.setText(str("5.0 ft to 6.0 ft"))
                elif str(age_tt) <= str(70):
                        self.Ideal_Weight.setText(str("75 Kg. to 77 Kg."))
                        self.Ideal_Height.setText(str("5.0 ft to 6.0 ft"))
if str(bmi) < str(15):
                self.Result_text.setText(str("You are very severely underweight")) 
        elif str(bmi) <= str(18.5):
                self.Result_text.setText(str("severely underweight")) 
        elif str(bmi) <= str(25):
                self.Result_text.setText(str("You are Normal (healthy weight)"))
        elif str(bmi) <= str(30):
                self.Result_text.setText(str(" You are overweight."))
        elif str(bmi) <= str(35):
                self.Result_text.setText(str(" You are moderately obese."))
        elif str(bmi) <= str(40):
                self.Result_text.setText(str(" You are severely obese."))
        elif str(bmi) > str(40):
                self.Result_text.setText(str(" You are very severely obese."))