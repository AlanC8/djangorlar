import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from users.models import User
from habits.models import ChallengeStatus, Challenge, Participant, CheckIn, Notification

class Command(BaseCommand):
    help = 'Fills the database with sample data'

    def handle(self, *args, **kwargs):
        
        fake = Faker('en_US')
        
        self.stdout.write("Deleting old data...")
        User.objects.exclude(is_superuser=True).delete()
        ChallengeStatus.objects.all().delete()
        Challenge.objects.all().delete()
        
        self.stdout.write("Creating new data...")

        users = []
        for _ in range(20):
            user = User.objects.create_user(
                email=fake.unique.email(),
                username=fake.unique.user_name(),
                password='password123'
            )
            users.append(user)

        statuses_data = ['Active', 'Completed', 'Failed']
        statuses = [ChallengeStatus.objects.create(name=s) for s in statuses_data]

        challenges = []
        for _ in range(20):
            creator = random.choice(users)
            start_date = fake.date_this_year()
            challenge = Challenge.objects.create(
                creator=creator,
                name=fake.sentence(nb_words=4),
                description=fake.text(max_nb_chars=200),
                start_date=start_date,
                end_date=start_date + timedelta(days=random.randint(7, 30)),
                status=random.choice(statuses)
            )
            challenges.append(challenge)

        for _ in range(40):
            user = random.choice(users)
            challenge = random.choice(challenges)
            
            if not Participant.objects.filter(user=user, challenge=challenge).exists():
                participant = Participant.objects.create(
                    user=user,
                    challenge=challenge,
                    current_streak=random.randint(0, 15)
                )
                
                for i in range(random.randint(1, 10)):
                    if challenge.start_date + timedelta(days=i) <= challenge.end_date:
                        CheckIn.objects.create(
                            participant=participant,
                            check_in_date=challenge.start_date + timedelta(days=i),
                            notes=fake.sentence(nb_words=6)
                        )

        for user in users:
            for _ in range(random.randint(0, 5)):
                Notification.objects.create(
                    user=user,
                    message=fake.sentence(nb_words=8),
                    is_read=random.choice([True, False])
                )

        self.stdout.write(self.style.SUCCESS('Successfully filled the database with data!'))