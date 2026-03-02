"""
Credibility & Contradiction
Courtroom logic game built using EasyGUI.

Player acts as a defense attorney and must identify contradictions
between witness testimony and evidence. Incorrect objections reduce
credibility. Losing all credibility loses the case.

This file defines the Level class and runs Level 1 and Level 2.
"""

from easygui import msgbox, buttonbox, choicebox, ynbox


# -------------------------
# LEVEL CLASS
# -------------------------


class Level:
    def __init__(self, starting_credibility, correct_evidence, correct_statement, testimonies, evidence, objection_messages, case_background, witness_introductions, witnesses):
        """
        Represents a level.

        Handles:
        - displaying background and evidence
        - presenting witness testimony
        - handling objections
        - tracking credibility
        - determining win/loss
        """

        # Player's current credibility score (decreases on mistakes)
        self.starting_credibility = starting_credibility
        # Index list of correct evidence for each testimony
        self.correct_evidence = correct_evidence
        # Index list of which statement is false in each testimony
        self.correct_statement = correct_statement
        # List of testimonies (each testimony is a list of statements)
        self.testimonies = testimonies
        # List of all evidence for the case
        self.evidence = evidence
        # List containing lists of messages shown after each successful objection
        self.objection_messages = objection_messages
        # Case background text
        self.case_background = case_background
        # List containing lists of intro dialogue shown before each witness
        self.witness_introductions = witness_introductions
        # Names of witnesses in order
        self.witnesses = witnesses

    def start_level(self):
        """
        Controls overall flow of the level.

        Shows background and evidence, then loops through each witness.
        Player must successfully object to the correct contradiction
        in each testimony to progress.

        Returns True if player wins the level, False if player loses.
        """
        self.background()
        self.view_evidence()
        index = 0
        # Loops through each witness testimony in order
        while index < len(self.testimonies):
            correct_evidence = self.evidence[self.correct_evidence[index]]
            statements = self.testimonies[index]
            correct_statement = statements[self.correct_statement[index]]
            current_witness = self.witnesses[index]
            self.introduce_witnesses(index)
            self.witness_statement(index)
            result = self.testimony(statements, self.evidence, correct_evidence, correct_statement, current_witness)
            # If player loses credibility, level ends immediately
            if result == False:
                break
            # Player successfully found the contradiction
            elif result == True:
                objection_message = self.objection_messages[index]
                self.objection_sustained(objection_message)
                index += 1
        # Player successfully cleared all testimonies and completed the level
        if index == len(self.testimonies):
            return True
        else:
            return False

    def witness_statement(self, index):
        """
        Displays the witness's full testimony before cross-examination begins.
        """
        full_statement = f"{self.witnesses[index]}:\n\n"
        for statement in self.testimonies[index]:
            full_statement += f"{statement} "
        msgbox(full_statement, "Credibility & Contradiction", "Continue")
        msgbox("Judge:\n\nThe defense may now cross-examine the witness.", "Credibility & Contradiction", "Continue")

    def introduce_witnesses(self, index):
        """
        Shows courtroom dialogue introducing the witness.
        """
        for introduction in self.witness_introductions[index]:
            msgbox(introduction, "Credibility & Contradiction", "Continue")

    def view_evidence(self):
        """
        Displays all evidence in numbered format for player review.
        """
        number = 1
        # Format evidence into numbered list for readability
        formatted_evidence = "Evidence for this case:\n\n"
        for evidence in self.evidence:
            formatted_evidence += f"{number}. {evidence}\n"
            number += 1
        msgbox(formatted_evidence, "Credibility & Contradiction", "Continue")

    def background(self):
        """
        Displays the background information of the case.
        """
        msgbox(self.case_background, "Credibility & Contradiction", "Continue")

    def objection_sustained(self, objection_message):
        """
        Reads out objection messages after a successful objection.
        """
        for message in objection_message:
            msgbox(message, "Credibility & Contradiction", "Continue")

    def testimony(self, statements, evidence, correct_evidence, correct_statement, current_witness):
        """
        Handles cross-examination of a witness.

        Player can:
        - move between statements
        - object to statements
        - review evidence or background

        Returns:
            True if correct objection made
            False if player loses
        """
        index = 0
        # Loop allows player to navigate statements freely
        while index < len(statements):
            choice = buttonbox(f"{current_witness}:\n\n{statements[index]}", "Credibility & Contradiction", ["Last Statement", "Next Statement", "Object", "Review Evidence", "Review Background"])
            # Calls objection function when player objects
            if choice == "Object":
                result = self.objection(statements[index], statements, evidence, correct_evidence, correct_statement, current_witness)
                if result == False:
                    return False
                elif result == True:
                    return True
                elif result == "canceled":
                    continue
                break
            # Calls view_evidence function when player wants to review evidence
            elif choice == "Review Evidence":
                self.view_evidence()
            # Calls background function when player wants to review background
            elif choice == "Review Background":
                self.background()
            elif choice == "Next Statement":
                index += 1
                if index >= len(statements):
                    index -= 1
                    msgbox("There are no further statements", "Credibility & Contradiction", "Continue")
            elif choice == "Last Statement":
                index -= 1
                if index < 0:
                    index = 0
                    msgbox("There are no previous statements", "Credibility & Contradiction", "Continue")

    def objection(self, statement, statements, evidence, correct_evidence, correct_statement, current_witness):
        """
        Handles objection logic.

        Checks whether player selected correct evidence
        against the correct statement.

        Reduces credibility if wrong.
        Ends game if credibility reaches zero.

        Returns:
            True if correct objection made
            False if player loses
            Testimony restarts if incorrect objection made without losing
            "canceled" if player cancels objection
        """
        msgbox("Objection!!!", "Credibility & Contradiction", "Continue")
        # Asks player to select evidence supporting objection
        answer = choicebox("Why do you object?", "Credibility & Contradiction", choices = evidence)
        # If player cancels objection
        if answer == None:
            return "canceled"
        elif statement == correct_statement:
            # Correct objection
            if answer == correct_evidence:
                return True
            # Incorrect objection
            else:
                # Incorrect evidence or incorrect objection reduces credibility
                self.starting_credibility -= 1
                msgbox(f"Judge:\n\nObjection overruled!", "Credibility & Contradiction", "Continue")
                msgbox(f"Your credibility score dropped to {self.starting_credibility}", "Credibility & Contradiction", "Continue")
                if self.starting_credibility == 0:
                    # Player loses if credibility hits 0
                    msgbox("The jury no longer trusts you.\nYou lose!", "Credibility & Contradiction", "Quit")
                    return False
                else:
                    # Restart testimony if player still has credibility
                    msgbox("Judge:\n\nThe witness may restart their testimony.", "Credibility & Contradiction", "Continue")
                    return self.testimony(statements, evidence, correct_evidence, correct_statement, current_witness)
        # Incorrect objection
        else:
            # Incorrect evidence or incorrect objection reduces credibility
            self.starting_credibility -= 1
            msgbox(f"Judge:\n\nObjection overruled!", "Credibility & Contradiction", "Continue")
            msgbox(f"Your credibility score dropped to {self.starting_credibility}", "Credibility & Contradiction", "Continue")
            if self.starting_credibility == 0:
                # Player loses if credibility hits 0
                msgbox("The jury no longer trusts you.\nYou lose!", "Credibility & Contradiction", "Quit")
                return False
            else:
                # Restart testimony if player still has credibility
                msgbox("Judge:\n\nThe witness may restart their testimony.", "Credibility & Contradiction", "Continue")
                return self.testimony(statements, evidence, correct_evidence, correct_statement, current_witness)


# -------------------------
# LEVEL 1 DATA
# -------------------------


first_statements = ["A janitor passed by me around 8:35 PM.", "I heard movement near the reference section around 8:40 PM.",
                    "I saw Jake walking toward the Special Collections room at 8:55 PM.", "A few minutes later I saw the door to the special collections room was still open.", "I left the building around 9:05 PM."]

second_statements = ["I entered the library at 8:15 PM.", "I saw Jake walking around at 8:25 PM.", "Jake seemed nervous about something.",
                     "I locked the Special Collections door at 8:30 PM.", "There was unusual motion detected in the reference section around 8:40 PM."]

third_statements = ["Maybe the person I saw at the time wasn't Jake, but I definitely saw him later.", "After locking the door, I put the key back right away at 8:32.",
                    "I saw Jake near the key's lock box around 8:55.", "The next morning the manuscript was gone.", "Jake must have stolen the key from the box."]

evidence = ["Special Collections door locked for the night at 8:30 PM", "Janitor entered building at 8:35 PM", "Detected movement near reference section at 8:40 PM", "Temperature sensor triggered at 8:42 PM",
            "Jake entered the library at 8:50 PM", "All students were out of the library by 9:05 PM", "Cameras show security returning the Special Collections key to the lockbox at 9:10 PM",]

correct_evidence = [0, 4, 6]
correct_statement = [3, 1, 1]

testimonies = [first_statements, second_statements, third_statements]

objection_message1 = ["Defense:\n\nThe door was locked at 8:30, and therefore could not have been open at the time.", "Judge:\n\nObjection sustained!"]

objection_message2 = ["Defense:\n\nJake entered the library at 8:50, and therefore would not have been there at 8:25.", "Judge:\n\nObjection sustained!"]

objection_message3 = ["Defense:\n\nThe Special Collections key was not checked into the lockbox until 9:10, and therefore you could not have returned it at 8:32.", "Judge:\n\nObjection sustained!",
                      "Defense:\n\nYour honor, the only person who would have had access to the Special Collections room when the manuscript was stolen would be Jeff Daniels.",
                      "Jeff Daniels:\n\nIf I confess to the crime now will that lessen my sentence?", "Judge:\n\nThat's not exactly how it works, but at least now we know that Jake is innocent.", "CASE DISMISSED"]

objection_messages = [objection_message1, objection_message2, objection_message3]

case_background = ("Case background:\n\nOn Tuesday night, a rare 18th-century manuscript disappeared from Anderson University’s Special Collections room. Only one key exists for the room, signed out from campus security. "
                   "The theft occurred between 8:00 PM and 9:30 PM. Your client, Jake Miller, was seen in the library that evening. Your job is to prove his innocence by catching contradictions in the witnesses’ statements using the evidence provided.")

witness1_introduction = ["Judge:\n\nCourt is now in session for the case of Anderson University v. Jake Miller. Prosecution, are you ready to proceed?",
                         "Prosecution:\n\nYes your honor. The prosecution would like to start by calling Samantha Jones, the library clerk on duty at the time of the crime, to the stand.", "Judge:\n\nYou may proceed."]

witness2_introduction = ["Prosecution:\n\nThe prosecution concedes that the door was locked at 8:30 PM. However, there is compelling evidence that Jake may have stolen the manuscript before this time. "
                         "The prosecution would now like to call Jeff Daniels, the security guard, to the stand.", "Judge:\n\nYou may proceed."]

witness3_introduction = ["Prosecution:\n\nThe prosecution concedes that Jake could not have stolen the book before 8:50 PM. However, there is a possibility that Jake stole the key from the lockbox. "
                         "Jeff Daniels has some information that could help substantiate this claim.", "Judge:\n\nYou may proceed."]

witnesses = ["Samantha Jones", "Jeff Daniels", "Jeff Daniels"]

witness_introductions = [witness1_introduction, witness2_introduction, witness3_introduction]


# -------------------------
# LEVEL 2 DATA
# -------------------------


level_two_first_statement = ["Emily is my best friend so I know she would never steal the drive.", "I was working in the library all night.", "I saw Nathan walking around the library at around 9:30 PM.",
                             "Emily left the server room at 9:15 PM and it was empty until about 9:45 PM when Nathan entered.", "I heard the drive had to have been stolen after 9:30 PM because it did something on the computer at that time."]

level_two_second_statement = ["I saw Nathan enter the library some time before 9:30 PM.", "I remember seeing him hanging around the server room around that time too.", "Emily's own testament and the statement from Sarah claim that Emily left at 9:15 PM.",
                              "Nathan must have been the one who entered the server room and triggered the 9:34 PM motion detection."]

level_two_third_statement = ["Emily has been working for the university's IT department for years so I wouldn't expect her to steal the drive now of all times.", "The card scan logs show Nathan entered the server room at 9:47 PM.",
                             "The drive must have been stolen before 10:00 PM as it did not execute its task at that time.", "I heard Nathan talking to himself in the server room around 9:55 PM.", "Nathan could have easily stolen the drive between 9:47 PM and 10:00 PM.",
                             "I assume the talking was a result of his guilty conscience."]

level_two_fourth_statement = ["I am still inclined to believe that Emily would not have stolen the drive.", "I admit that the flash drive could only have been stolen when the computer was powered off.",
                              "The record stipulates that the computer was powered off a second time after 10:30 PM.", "Nathan did not leave the library until 10:37 PM.", "Therefore, he could have stolen the drive between 10:30 PM and 10:37 PM."]

level_two_testimonies = [level_two_first_statement, level_two_second_statement, level_two_third_statement, level_two_fourth_statement]

level_two_correct_statements = [3, 3, 4, 4]

level_two_background = ("Case background:\n\nOn October 14th, an important university flash drive was stolen from the server room (inside the library) some time after 9:30 PM. The only two people to enter the server room that night were Emily Harper and Nathan Cole. "
                        "Emily Harper claims she left the server room at 9:15 PM. Nathan Cole, your client, has been accused of stealing the flash drive from the university. It is your job to prove his innocence.")

level_two_evidence = ["Card scanner log shows Emily Harper entering the server room at 8:02 PM", "Card scanner log shows Nathan Cole entering the server room at 9:47 PM", "Server room doors lock automatically when closed", "Entering the server room always requires a card scan",
                      "Interior motion sensor detected movement inside the server room at 9:12 PM, 9:34 PM, 9:53 PM, and 10:35 PM", "Cameras show Nathan entering the library at 9:27 PM", "Cameras show Nathan standing around the server room at 9:29 PM",
                      "Cameras show Nathan exiting the library at 10:37 PM", "The flash drive runs an automated task every 30 minutes", "The task executed successfully at 9:30 PM but did not execute at 10:00 PM",
                      "The computer keeps records of when flash drives are ejected unless the system is powered off", "There was no record of the flash drive being ejected",
                      "The system was powered down automatically from 9:30 PM to 9:45 PM for a software update and again at 10:30 PM when the library closed"]

level_two_correct_evidence = [4, 1, 12, 9]

level_two_objection_message1 = ["Defense:\n\nThere was motion detected in the server room at 9:34 PM, and therefore it could not have been empty from 9:15 PM to 9:45 PM.", "Judge:\n\nObjection sustained!"]

level_two_objection_message2 = ["Defense:\n\nThe scan card logs show Nathan did not enter the server room until 9:47 PM. Therefore, he could not have been in the room at 9:34 PM.", "Judge:\n\nObjection sustained!"]

level_two_objection_message3 = ["Defense:\n\nThe drive could have only been stolen while the system was powered down because there was no record of the drive being ejected. The system was not powered down from 9:47 PM to 10:00 PM. "
                                "Therefore, the crime could not have happened during this time period.", "Judge:\n\nObjection sustained!"]

level_two_objection_message4 = ["Defense:\n\nIn his last testimony the witness admitted that the drive must have been stolen before 10:00 PM. The drive's task did not execute at 10:00 PM because it had already been stolen. "
                                "Therefore, the drive could not have been taken after 10:30 PM. Considering all of the facts, the drive could have only been stolen between 9:30 PM and 9:45 PM. "
                                "Nathan Cole was not in the server room during this time period, and therefore could not have stolen the drive.", "Judge:\n\nObjection sustained!",
                                "Judge:\n\nThe only person in the server room when the drive was stolen was Emily Harper; her trial will happen in the near future. For now, we at least know that Nathan Cole is innocent.", "CASE DISMISSED"]

level_two_objection_messages = [level_two_objection_message1, level_two_objection_message2, level_two_objection_message3, level_two_objection_message4]

level_two_witness1_introduction = ["Judge:\n\nCourt is now in session for the case of Anderson University v. Nathan Cole. Prosecution, are you ready to proceed?",
                                   "Prosecution:\n\nYes your honor. The prosecution would like to start by calling Sarah Ross, one of the library clerks on duty at the time of the crime, to the stand.", "Judge:\n\nYou may proceed."]

level_two_witness2_introduction = ["Prosecution:\n\nThe prosecution concedes that the server room motion sensor went off at 9:34 PM. However, there is compelling evidence that Nathan could have triggered this sensor. "
                                   "This claim is substantiated by what Natasha Holman, the other library clerk on duty, saw that night. The prosecution would like to call Natasha Holman to the stand.", "Judge:\n\nYou may proceed."]

level_two_witness3_introduction = ["Prosecution:\n\nThe prosecution concedes that Emily Harper was in the server room at 9:34 PM. However, there is still reason to believe that Nathan is a more likely suspect for stealing the drive. "
                                   "The prosecution would like to call Johnathan Park, Emily Harper's boss and the head of the IT department, to the stand.", "Judge:\n\nYou may proceed."]

level_two_witness4_introduction = ["Prosecution:\n\nThe prosecution concedes that the drive could have only been stolen while the system was powered down. However, it is still possible Nathan is responsible. "
                                   "We would like to continue with Johnathan's testimony.", "Judge:\n\nYou may proceed."]

level_two_witness_introductions = [level_two_witness1_introduction, level_two_witness2_introduction, level_two_witness3_introduction, level_two_witness4_introduction]

level_two_witnesses = ["Sarah Ross", "Natasha Holman", "Johnathan Park", "Johnathan Park"]


# -------------------------
# GAME START
# -------------------------


welcome = ("Welcome to Credibility & Contradiction!\n\nYou are a fresh graduate of Stanford law school preparing for your very first case. For each case you take on you will be given some background information and evidence "
           "that has been deemed by the court to be the objective facts of the record. In the courtroom, you will listen to witnesses deliver their testimony of what happened. "
           "When you get the opportunity to cross-examine the witnesses, your job is to object (by clicking the object button) to any false statements they make and provide the evidence that proves they are lying. If you ever forget any background information or evidence "
           "just click their respective buttons to review the information.")

credibility_explanation = ("As a defense attorney, maintaining your credibility is essential to success. You will start with a credibility score of 1, 2, or 3 depending on what difficulty you select. "
                           "Every time you make a mistake, such as objecting to a true statement, you lose one credibility point. Your credibility score resets at the start of each new case. "
                           "If your credibility score ever gets to 0, the jury will lose faith in your arguments and you will lose the case.")

msgbox(welcome, "Credibility & Contradiction", "Continue")
msgbox(credibility_explanation, "Credibility & Contradiction", "Continue")

# Set starting credibility based on difficulty
difficulty = buttonbox("Select Difficulty", "Credibility & Contradiction", ["Easy", "Medium", "Hard"])
if difficulty == "Easy":
    starting_credibility = 3
elif difficulty == "Medium":
    starting_credibility = 2
else:
    starting_credibility = 1

msgbox(f"You have a starting credibility score of {starting_credibility} credibility. Every time you make a mistake this score will drop.\n\nGood luck on your first case!", "Credibility & Contradiction", "Continue")

# Create and start Level 1
level_1 = Level(starting_credibility, correct_evidence, correct_statement, testimonies, evidence, objection_messages, case_background, witness_introductions, witnesses)
win = level_1.start_level()

# If player wins Level 1, Level 2 is offered
if win == True:
    if ynbox("Would you like to try a harder case?", "Credibility & Contradiction"):
        msgbox(f"Your credibility score has been reset to {starting_credibility} credibility.", "Credibility & Contradiction", "Continue")
        level_2 = Level(starting_credibility, level_two_correct_evidence, level_two_correct_statements, level_two_testimonies, level_two_evidence, level_two_objection_messages, level_two_background, level_two_witness_introductions, level_two_witnesses)
        win2 = level_2.start_level()
        if win2 == True:
            msgbox("You win!\n\nThank you for playing!", "Credibility & Contradiction", "Quit")
    else:
        msgbox("Thank you for playing!", "Credibility & Contradiction", "Quit")