from django.shortcuts import render

def home(request):
    context = {
        'sections': [
            {'title': 'Classes', 'description': 'Explore our classes and take your fitness to the next level.', 'image': 'workouts.png', 'url': 'classes:classes'},
            {'title': 'Workouts', 'description': 'Discover a variety of workouts for every fitness level.', 'image': 'workouts.png', 'url': 'workouts:workouts'},
            {'title': 'Community', 'description': 'Join our supportive community and achieve your goals together.', 'image': 'workouts.png', 'url': 'community:community'},
        ],
        'testimonials': [
            {'name': 'John D.', 'text': 'FitLife has transformed my lifestyle. The classes are amazing and the community is so supportive!'},
            {'name': 'Sarah M.', 'text': "I've never felt stronger or more confident. The trainers here are top-notch!"},
            {'name': 'Mike R.', 'text': 'The variety of workouts keeps me motivated. I look forward to every session at FitLife.'},
        ],
        'quick_links': [
            {'title': 'Class Schedule', 'url': 'classes:classes'},
            {'title': 'Membership Plans', 'url': 'classes:classes'},
            {'title': 'Nutrition Tips', 'url': 'classes:classes'},
            {'title': 'Success Stories', 'url': 'classes:classes'},
        ],
    }
    return render(request, 'home.html', context)
