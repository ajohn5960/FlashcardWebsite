from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import UserProfile
from set.models import Set


'''
STEPS TO DELETE ACCOUNT
- in settings page at bottom -> delete account btn
- delete account page 
- authenticate it's user -> authenticate or cancel
- delete account? -> delete and cancel btn
- account has been deleted -> home btn
'''



@login_required
def profile_detail_view(request):
    current_user = request.user
    print("User Id: " + str(current_user.id))
    user_profile = get_object_or_404(UserProfile, user_id=current_user.id)  
    set_count = Set.objects.filter(user=current_user).count()
    context = {
        "current_user" :current_user,
        "user_profile" : user_profile,
        "set_count" : set_count
    }
    return render(request, "profile.html", context)







#  first_name, last_name, num_stacks, user_id, user_id_id 
