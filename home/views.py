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
            {'title': 'Stay Hydrated', 'description': 'Drinking plenty of water throughout the day is essential for maintaining optimal hydration levels. It helps regulate body temperature, keeps joints lubricated, and delivers nutrients to cells. Aim for at least 8 glasses a day, and more if you are active or in a hot environment.'},
            {'title': 'Balanced Diet', 'description': 'Incorporating a variety of foods into your diet is crucial for balanced nutrition. Aim to include fruits, vegetables, whole grains, lean proteins, and healthy fats in your meals. This variety ensures you get a wide range of nutrients that support overall health and wellness.'},
            {'title': 'Mindful Eating', 'description': 'Paying attention to your hunger cues and eating mindfully can significantly improve your relationship with food. Try to eat slowly, savor each bite, and eliminate distractions during meals. This practice can help you recognize when you are truly hungry or full, leading to healthier eating habits.'},
            {'title': 'Eat More Fiber', 'description': 'Fiber is an essential part of a healthy diet, helping to promote digestive health and prevent constipation. Foods rich in fiber, such as fruits, vegetables, legumes, and whole grains, can also keep you feeling full longer, aiding in weight management.'},
            {'title': 'Limit Processed Foods', 'description': 'Processed foods often contain high levels of added sugars, unhealthy fats, and sodium. Reducing your intake of these foods can lead to better health outcomes. Focus on whole, minimally processed foods for better nutrition and energy levels.'},
            {'title': 'Healthy Snacking', 'description': 'Choosing healthy snacks can help maintain your energy levels throughout the day. Opt for snacks like nuts, yogurt, fruits, or veggie sticks with hummus. These options are not only nutritious but can also satisfy your cravings without excessive calories.'},
            {'title': 'Plan Your Meals', 'description': 'Planning your meals ahead of time can help you make healthier choices and avoid last-minute unhealthy options. Try to set aside some time each week to prepare meals and snacks, ensuring you have nutritious options readily available.'},
            {'title': 'Listen to Your Body', 'description': 'Understanding your body’s signals is key to healthy eating. Pay attention to how different foods make you feel and adjust your diet accordingly. This awareness can help you identify which foods energize you and which may cause discomfort.'},
        ],
        'quick_links': [
            {'title': 'Class Schedule', 'url': 'classes:classes'},
            {'title': 'Membership Plans', 'url': 'classes:classes'},
            {'title': 'Nutrition Tips', 'url': 'classes:classes'},
            {'title': 'Success Stories', 'url': 'classes:classes'},
        ],
    }
    return render(request, 'home.html', context)