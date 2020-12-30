//except for this line, this is what interpret_source.load_src returns
importgreenfoot.*;//(World,Actor,GreenfootImage,GreenfootandMouseInfo)
classRoverextendsActor
{
Displayanzeige;
voidact()
{
S66Nr3(7);
}
voidfahreUmHuegel(Stringrichtung)
{
Stringpri;
Stringsec;
if(richtung.equals("Hoch")){
pri="links";
sec="rechts";
}else{
if(richtung.equals("Runter")){
pri="rechts";
sec="links";
}else{
nachricht("JUNGEDUSPAST!");
return;
}
}
drehe(pri);
fahre();
drehe(sec);
fahre();
fahre();
drehe(sec);
fahre();
drehe(pri);
}
voidfahreBisHuegel()
{
while(!huegelVorhanden("vorne"))
{
fahre();
}
}
voidfahreZeileDreheHoch()
{
fahreBisHuegel();
fahreUmHuegel("Hoch");
fahreBisHuegel();
drehe("um");
fahreBisHuegel();
fahreUmHuegel("Runter");
fahreBisHuegel();
drehe("rechts");
fahre();
drehe("rechts");
}
voidfahreZeileDreheRunter(booleangeheInNächsteZeile)
{
fahreBisHuegel();
fahreUmHuegel("Runter");
fahreBisHuegel();
drehe("um");
fahreBisHuegel();
fahreUmHuegel("Hoch");
fahreBisHuegel();
if(geheInNächsteZeile){
drehe("rechts");
fahre();
drehe("rechts");
}else{
drehe("um");
}
}
voidS66Nr3(intanzahlZeilen)
{
if(anzahlZeilen<3){
nachricht("IchmussmindestensdreiZeilenfahren!:(");
return;
}
fahreZeileDreheHoch();
for(inti=1;i<anzahlZeilen-1;i++){
fahreZeileDreheRunter(true);
}
fahreZeileDreheRunter(false);
}
voidfahre()
{
intposX=getX();
intposY=getY();
if(huegelVorhanden("vorne"))
{
nachricht("Zusteil!");
}
elseif(getRotation()==270&&getY()==1)
{
nachricht("Ichkannmichnichtbewegen");
}
else
{
move(1);
Greenfoot.delay(1);
}
if(posX==getX()&&posY==getY()&&!huegelVorhanden("vorne"))
{
nachricht("Ichkannmichnichtbewegen");
}
}
voiddrehe(Stringrichtung)
{
if(richtung.equals("rechts")){
setRotation(getRotation()+90);
}elseif(richtung.equals("links")){
setRotation(getRotation()-90);
}elseif(richtung.equals("um")){
setRotation(getRotation()+180);
}else{
nachricht("KeinenKorrekteRichtunggegeben!");
}
}
booleangesteinVorhanden()
{
if(getOneIntersectingObject(Gestein.class)!=null)
{
nachricht("Gesteingefunden!");
returntrue;
}
returnfalse;
}
booleanhuegelVorhanden(Stringrichtung)
{
introt=getRotation();
if(richtung=="vorne"&&rot==0||richtung=="rechts"&&rot==270||richtung=="links"&&rot==90)
{
if(getOneObjectAtOffset(1,0,Huegel.class)!=null&&((Huegel)getOneObjectAtOffset(1,0,Huegel.class)).getSteigung()>30)
{
returntrue;
}
}
if(richtung=="vorne"&&rot==180||richtung=="rechts"&&rot==90||richtung=="links"&&rot==270)
{
if(getOneObjectAtOffset(-1,0,Huegel.class)!=null&&((Huegel)getOneObjectAtOffset(-1,0,Huegel.class)).getSteigung()>30)
{
returntrue;
}
}
if(richtung=="vorne"&&rot==90||richtung=="rechts"&&rot==0||richtung=="links"&&rot==180)
{
if(getOneObjectAtOffset(0,1,Huegel.class)!=null&&((Huegel)getOneObjectAtOffset(0,1,Huegel.class)).getSteigung()>30)
{
returntrue;
}
}
if(richtung=="vorne"&&rot==270||richtung=="rechts"&&rot==180||richtung=="links"&&rot==0)
{
if(getOneObjectAtOffset(0,-1,Huegel.class)!=null&&((Huegel)getOneObjectAtOffset(0,-1,Huegel.class)).getSteigung()>30)
{
returntrue;
}
}
if(richtung!="vorne"&&richtung!="links"&&richtung!="rechts")
{
nachricht("Befehlnichtkorrekt!");
}
returnfalse;
}
voidanalysiereGestein()
{
if(gesteinVorhanden())
{
nachricht("Gesteinuntersucht!Wassergehaltist"+((Gestein)getOneIntersectingObject(Gestein.class)).getWassergehalt()+"%.");
Greenfoot.delay(1);
removeTouching(Gestein.class);
}
else
{
nachricht("HieristkeinGestein");
}
}
voidsetzeMarke()
{
getWorld().addObject(newMarke(),getX(),getY());
}
booleanmarkeVorhanden()
{
if(getOneIntersectingObject(Marke.class)!=null)
{
returntrue;
}
returnfalse;
}
voidentferneMarke()
{
if(markeVorhanden())
{
removeTouching(Marke.class);
}
}
voidnachricht(StringpText)
{
if(anzeige!=null)
{
anzeige.anzeigen(pText);
Greenfoot.delay(1);
anzeige.loeschen();
}
}
voiddisplayAusschalten()
{
getWorld().removeObject(anzeige);
}
protectedvoidaddedToWorld(Worldworld)
{
setImage("images/rover.png");
world=getWorld();
anzeige=newDisplay();
anzeige.setImage("images/nachricht.png");
world.addObject(anzeige,7,0);
if(getY()==0)
{
setLocation(getX(),1);
}
anzeige.anzeigen("Ichbinbereit");
}
classDisplayextendsActor
{
GreenfootImagebild;
Display()
{
bild=getImage();
}
voidact()
{
}
voidanzeigen(StringpText)
{
loeschen();
getImage().drawImage(newGreenfootImage(pText,25,Color.BLACK,newColor(0,0,0,0)),10,10);
}
voidloeschen()
{
getImage().clear();
setImage("images/nachricht.png");
}
}
classDirection{
Direction(intval){
this.value=val;
}
intvalue;
};
}
