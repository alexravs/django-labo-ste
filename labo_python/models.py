from django.db import models

class Candidat(models.Model):
    id        = models.AutoField(db_column="id", primary_key=True, null=False) 
    prenom      = models.CharField(db_column="prenom", max_length=30, null=False) 
    nom         = models.CharField(db_column="nom", max_length=30, null=False)
    ddn         = models.DateField(db_column="ddn", null=False)
    sexe        = models.CharField(db_column="sexe", max_length=30, null=False)
    adresse     = models.CharField(db_column="adresse", max_length=50, null=False)
    cp          = models.CharField(db_column="cp", max_length=10, null=False)
    loc         = models.CharField(db_column="loc", max_length=50, null=False)
    pays        = models.CharField(db_column="pays", max_length=50, null=False)
    email       = models.CharField(db_column="email", max_length=30, null=False) 
    tel         = models.CharField(db_column="tel", max_length=30, null=False)
    fax         = models.CharField(db_column="fax", max_length=30, null=False)
    gsm         = models.CharField(db_column="gsm", max_length=30, null=False)
    login       = models.CharField(db_column="login", max_length=30, null=False)
    pwd         = models.CharField(db_column="pwd", max_length=30, null=False)
    date_inscription = models.DateField(db_column="date_inscription", null=False )
    date_dernier_acces = models.DateField(db_column="date_dernier_acces", null=False )
    
    
    
    class Meta() : #django recherche à quel table correpond la classe
        db_table = "candidats"
    
class DAOCandidat(object): 
      
    @staticmethod
    def getCandidatById(idCandidat):
        candidat = None
        try :
            candidat = Candidat.objects.get(id=idCandidat)
        except candidat.DoesNotExist:
            print("Le candidat avec l'id {0} n'existe pas".format(id))
        return candidat
    
    
    
    @staticmethod 
    def insertCandidat(prenom,nom,ddn, sexe, adresse, cp,loc, pays, email, tel, fax, gsm, login, pwd):
        import django.utils      

        
        c = Candidat()
        c.prenom = prenom
        c.nom = nom
        c.ddn = ddn
        c.sexe = sexe
        c.adresse = adresse
        c.cp = cp
        c.loc = loc
        c.pays = pays
        c.email = email
        c.tel = tel
        c.fax = fax
        c.gsm = gsm
        c.login = login
        c.pwd = pwd
        c.date_inscription = django.utils.timezone.now() 
        c.date_dernier_acces = django.utils.timezone.now() 
        try:
            c.save()
        except:
            raise Exception("déjà là mon gars")
        