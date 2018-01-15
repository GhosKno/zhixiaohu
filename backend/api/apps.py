from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'


class ApiCli():
    @classmethod
    def process_profile(cls, guest, user):
        if guest.is_authenticated:
            user.profile.is_watch = guest.profile\
                .watchedUser.filter(
                id=user.id
            ).exists()
        else:
            user.profile.is_watch = False
    
    @classmethod
    def process_question(cls, question):
        question.answer_count = question.answers.count()
        question.watch_count = question.watchedUser.count()
    
    @classmethod
    def process_answer(cls, answer, guest):
        answer.userSummary = answer.author.profile
        answer.comment_count = answer.comments.count()
        if guest.is_authenticated:
            answer.has_approve = guest.profile.agreed.filter(id=answer.id).exists()
            answer.has_against = guest.profile.disagreed.filter(id=answer.id).exists()
            answer.has_favorite = guest.profile.favorites.filter(id=answer.id).exists()
        else:
            answer.has_approve = False
            answer.has_against = False
            answer.has_favorite = False

    @classmethod
    def process_comment(cls, comment):
        profile = comment.author.profile
        comment.userSummary = profile