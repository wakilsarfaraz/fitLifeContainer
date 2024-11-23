from django.shortcuts import render

def home(request):
    context = {
        'sections': [
            {'title': 'Classes', 'description': 'Explore our classes and take your fitness to the next level.', 'image': 'classes.png', 'url': 'classes:classes'},
            {'title': 'Workouts', 'description': 'Discover a variety of workouts for every fitness level.', 'image': 'workouts.png', 'url': 'workouts:workouts'},
            {'title': 'Community', 'description': 'Join our supportive community and achieve your goals together.', 'image': 'community.png', 'url': 'community:community'},
        ],
        'testimonials': [
            {'name': 'John D.', 'text': 'FitLife has transformed my lifestyle. The classes are amazing and the community is so supportive!', 'image': 'user1.jpg'},
            {'name': 'Sarah M.', 'text': "I've never felt stronger or more confident. The trainers here are top-notch!", 'image': 'user2.jpg'},
            {'name': 'Mike R.', 'text': 'The variety of workouts keeps me motivated. I look forward to every session at FitLife.', 'image': 'user3.webp'},
        ],
        'nutrition_tips': [
            {'title': 'Stay Hydrated', 'description': 'Drink plenty of water throughout the day to stay hydrated.', 'image': 'water.jpeg'},
            {'title': 'Balanced Diet', 'description': 'Incorporate a variety of foods into your diet for balanced nutrition.', 'image': 'diet.jpeg'},
            {'title': 'Mindful Eating', 'description': 'Pay attention to your hunger cues and eat mindfully.', 'image': 'diet2.jpeg'},
        ],
        'quick_links': [
            {'title': 'Class Schedule', 'url': 'classes:classes'},
            {'title': 'Membership Plans', 'url': 'classes:classes'},
            {'title': 'Nutrition Tips', 'url': 'classes:classes'},
            {'title': 'Success Stories', 'url': 'classes:classes'},
        ],
    }
    return render(request, 'home.html', context)