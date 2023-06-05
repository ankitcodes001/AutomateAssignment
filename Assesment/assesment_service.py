from .models import Question
from .models import QuestionPaper

class QuestionService:
    def get_all_questions():
        return Question.objects.all()

    def create_question(data):
        question = Question.objects.create(
            question_text=data['question_text'],
            options=data.get('options', ''),
            correct_answer=data['correct_answer'],
            difficulty_level=data['difficulty_level']
        )
        return question

    def get_question_by_id(question_id):
        try:
            return Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return None

    def update_question(question, data):
        question.question_text = data.get('question_text', question.question_text)
        question.options = data.get('options', question.options)
        question.correct_answer = data.get('correct_answer', question.correct_answer)
        question.difficulty_level = data.get('difficulty_level', question.difficulty_level)
        # Update other fields as needed
        question.save()
        return question

    def delete_question(question):
        question.delete()
        
        

class QuestionPaperService:
    def get_all_question_papers():
        return QuestionPaper.objects.all()

    def create_question_paper(data):
        question_paper = QuestionPaper.objects.create(
            title=data['title'],
            duration=data['duration'],
            total_marks=data['total_marks']
        )
        # Add logic to associate questions with the question paper
        question_paper.questions.set(data['questions'])
        return question_paper

    def get_question_paper_by_id(paper_id):
        try:
            return QuestionPaper.objects.get(id=paper_id)
        except QuestionPaper.DoesNotExist:
            return None

    def update_question_paper(question_paper, data):
        question_paper.title = data.get('title', question_paper.title)
        question_paper.duration = data.get('duration', question_paper.duration)
        question_paper.total_marks = data.get('total_marks', question_paper.total_marks)
        # Update other fields as needed
        # Add logic to update associated questions
        question_paper.save()
        return question_paper

    def delete_question_paper(question_paper):
        question_paper.delete()
            
