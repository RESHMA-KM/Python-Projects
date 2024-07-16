#!/usr/bin/env python
# coding: utf-8

# # Tkinter_Quiz Maker
# 
# 

# In[2]:


import tkinter as tk
from tkinter import messagebox, ttk

quiz_data = [
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "choices": ["William Shakespeare", "Jane Austen", "Leo Tolstoy", "Charles Dickens"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "choices": ["Jupiter", "Mars", "Saturn", "Neptune"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
        "answer": "Blue Whale"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "Which country is famous for the Great Wall?",
        "choices": ["China", "Japan", "India", "United States"],
        "answer": "China"
    },
    {
        "question": "What is the capital of Australia?",
        "choices": ["Sydney", "Canberra", "Melbourne", "Brisbane"],
        "answer": "Canberra"
    },
   
    {
        "question": "What is the largest desert in the world?",
        "choices": ["Gobi Desert", "Sahara Desert", "Arabian Desert", "Antarctica"],
        "answer": "Sahara Desert"
    },
    {
        "question": "Which bird is known for its long neck?",
        "choices": ["Penguin", "Ostrich", "Flamingo", "Albatross"],
        "answer": "Ostrich"
    },
    {
        "question": "Which element has the chemical symbol 'H'?",
        "choices": ["Hydrogen", "Helium", "Hafnium", "Holmium"],
        "answer": "Hydrogen"
    }
]

class QuizMakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Maker")
        self.root.geometry("600x600")

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 20))
        self.style.configure("TButton", font=("Helvetica", 16))

        self.current_question = 0
        self.score = 0

        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        self.qs_label = ttk.Label(
            self.root,
            anchor="center",
            wraplength=500,
            padding=10
        )
        self.qs_label.pack(pady=10)

        
        self.choice_btns = []
        for i in range(4):
            button = ttk.Button(
                self.root,
                command=lambda i=i: self.check_answer(i)
            )
            button.pack(pady=5)
            self.choice_btns.append(button)

    
        self.feedback_label = ttk.Label(
            self.root,
            anchor="center",
            padding=10
        )
        self.feedback_label.pack(pady=10)

    
        self.correct_answer_label = ttk.Label(
            self.root,
            anchor="center",
            padding=10,
            foreground="blue"
        )
        self.correct_answer_label.pack(pady=10)

    
        self.score_label = ttk.Label(
            self.root,
            text="Score: {}/{}".format(self.score, len(quiz_data)),
            anchor="center",
            padding=10
        )
        self.score_label.pack(pady=10)

        
        self.next_btn = ttk.Button(
            self.root,
            text="Next",
            command=self.next_question,
            state="disabled"
        )
        self.next_btn.pack(pady=10)

    
        ttk.Button(
            self.root,
            text="Add Question",
            command=self.add_question
        ).pack(pady=10)

    
        ttk.Button(
            self.root,
            text="Edit Question",
            command=self.edit_question
        ).pack(pady=10)

    
        ttk.Button(
            self.root,
            text="Delete Question",
            command=self.delete_question
        ).pack(pady=10)

    def show_question(self):
        question = quiz_data[self.current_question]
        self.qs_label.config(text=question["question"])

        choices = question["choices"]
        for i in range(4):
            self.choice_btns[i].config(text=choices[i], state="normal")

        self.feedback_label.config(text="")
        self.correct_answer_label.config(text="")

        self.next_btn.config(state="disabled")

    def check_answer(self, choice):
        question = quiz_data[self.current_question]
        selected_choice = self.choice_btns[choice].cget("text")

        if selected_choice == question["answer"]:
            self.score += 1
            self.score_label.config(text="Score: {}/{}".format(self.score, len(quiz_data)))
            self.feedback_label.config(text="Correct!", foreground="green")
        else:
            correct_answer = question["answer"]
            self.feedback_label.config(text="Incorrect!", foreground="red")
            self.correct_answer_label.config(text="Correct answer: {}".format(correct_answer))

        for button in self.choice_btns:
            button.config(state="disabled")
        self.next_btn.config(state="normal")

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(quiz_data):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Completed", "Quiz Completed! Final score: {}/{}".format(self.score, len(quiz_data)))
            self.root.destroy()

    def add_question(self):
        pass  

    def edit_question(self):
    
        pass 

    def delete_question(self):
        pass  
    
root = tk.Tk()
app = QuizMakerApp(root)
root.mainloop()


# In[ ]:




