from django.http import HttpResponse
from django.shortcuts import render_to_response
from labo_python.models import DAOCandidat, Candidat


def verifConnexion(requete):
    connected = None
    user = None
    if requete.session.get('candidat') is not None:
        user = Candidat.objects.get(id = requete.session.get('candidat'))
        connected = True
        
    return {"connected": connected, "user": user}

def base(requete):
    connexion = verifConnexion(requete)
    connected = connexion.get("connected")
    user = connexion.get("user")    
        #nom = user.nom
        #prenom = user.prenom
    
    return render_to_response("home.html", locals())

def login(requete):
    connexion = verifConnexion(requete)
    connected = connexion.get("connected")
    user = connexion.get("user") 
    
    return render_to_response("login.html")

def sign_up(requete):
    connexion = verifConnexion(requete)
    connected = connexion.get("connected")
    user = connexion.get("user") 
    
    return render_to_response("sign_up.html" )

def sign_up_done(requete):
    connexion = verifConnexion(requete)
    connected = connexion.get("connected")
    user = connexion.get("user") 
    
    prenom = requete.POST.get("prenom", None)
    nom = requete.POST.get("nom", None)
    ddn = requete.POST.get("ddn", None)
    sexe = requete.POST.get("sexe", None)
    adresse = requete.POST.get("adresse", None)
    cp = requete.POST.get("cp", None)
    loc = requete.POST.get("loc", None)
    pays = requete.POST.get("pays", None)
    email = requete.POST.get("email", None)
    tel = requete.POST.get("tel", None)
    fax = requete.POST.get("fax", None)
    gsm = requete.POST.get("gsm", None)
    login = requete.POST.get("login", None)
    pwd = requete.POST.get("password", None)
    try:
        c = DAOCandidat.insertCandidat(prenom, nom, ddn, sexe, adresse, cp, loc, pays, email, tel, fax, gsm, login, pwd)
        return render_to_response("sign_up_done.html", locals())
    except:
        message = str(Exception())
        messageToRender = True
        return render_to_response("sign_up.html", {"message": message, "messageToRender":messageToRender})
    
def log_in_done(requete):
    
    
    password = requete.POST.get("password", None)
    user = Candidat.objects.get(login = requete.POST.get("username", None))
    if user.pwd == password:
        import django.utils
        requete.session["candidat"] = user.id
        user.date_dernier_acces = django.utils.timezone.now()
        user.save()
        connected = True
        return render_to_response("logged_on.html", locals())
    else:
        return login(requete)
    
    
    
def log_out(requete):
    
    requete.session.flush()
    return base(requete) 