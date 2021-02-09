// import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

// //Comment that the interpreter may never know of

// public class Rover extends Actor
// {
//     private Display anzeige;

//     /**
//      * this function is to be implemented by the user
//      * depending on the needed actions
//      */

//     public Display getDisplay()
//     {
//         return anzeige;
//     }

//     public void act()
//     {
//         S66Nr3(7);
//     }

//     private void fahreUmHuegel(String richtung)
//     {
//         String pri;
//         String sec;
//         if(richtung.equals("Hoch")) {
//             pri = "links";
//             sec = "rechts";
//         } else if (richtung.equals("Runter")) {
//             pri = "rechts";
//             sec = "links";
//         } else {
//             nachricht("JUNGE DU SPAST!");
//             return;
//         }
//         drehe(pri);
//         fahre();
//         drehe(sec);
//         fahre();
//         fahre();
//         drehe(sec);
//         fahre();
//         drehe(pri);
//     }

//     private void fahreBisHuegel()
//     {
//         while(!huegelVorhanden("vorne"))
//         {
//             fahre();
//         }
//     }

//     private void fahreZeileDreheHoch()
//     {
//         fahreBisHuegel();
//         fahreUmHuegel("Hoch");
//         fahreBisHuegel();
//         drehe("um");

//         fahreBisHuegel();
//         fahreUmHuegel("Runter");
//         fahreBisHuegel();
//         drehe("rechts");
//         fahre();
//         drehe("rechts");
//     }

//     private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
//     {
//         fahreBisHuegel();
//         fahreUmHuegel("Runter");
//         fahreBisHuegel();
//         drehe("um");

//         fahreBisHuegel();
//         fahreUmHuegel("Hoch");
//         fahreBisHuegel();
//         if(geheInNächsteZeile) {
//             drehe("rechts");
//             fahre();
//             drehe("rechts");
//         } else {
//             drehe("um");
//         }
//     }

//     private void S66Nr3(int anzahlZeilen)
//     {
//         if(anzahlZeilen < 3) {
//             nachricht("Ich muss mindestens drei Zeilen fahren! :(");
//             return;
//         }
//         int i = 1;
//         fahreZeileDreheHoch();
//         for(; i < anzahlZeilen-1; i++) {
//             fahreZeileDreheRunter(true);
//         }
//         fahreZeileDreheRunter(false);
//     }

//     /**
//      * Der Rover bewegt sich ein Feld in Fahrtrichtung weiter.
//      * Sollte sich in Fahrtrichtung ein Objekt der Klasse Huegel befinden oder er sich an der Grenze der Welt befinden,
//      * dann erscheint eine entsprechende Meldung auf dem Display.
//      */
//     public void fahre()
//     {
//         int posX = getX();
//         int posY = getY();

//         if(huegelVorhanden("vorne"))
//         {
//             nachricht("Zu steil!");
//         }
//         else if(getRotation()==270 && getY()==1)
//         {
//             nachricht("Ich kann mich nicht bewegen");
//         }
//         else
//         {
//             move(1);
//             Greenfoot.delay(1);
//         }

//         if(posX==getX()&&posY==getY()&&!huegelVorhanden("vorne"))
//         {
//             nachricht("Ich kann mich nicht bewegen");
//         }
//     }

//     /**
//      * Der Rover dreht sich um 90 Grad in die Richtung, die mit richtung (ï¿œlinksï¿œ oder ï¿œrechtsï¿œ) ï¿œbergeben wurde.
//      * Sollte ein anderer Text (String) als "rechts" oder "links" ï¿œbergeben werden, dann erscheint eine entsprechende Meldung auf dem Display.
//      */
//     public void drehe(String richtung)
//     {
//         if(richtung.equals("rechts")){
//             setRotation(getRotation()+90);
//         }else if(richtung.equals("links")){
//             setRotation(getRotation()-90);
//         } else if(richtung.equals("um")) {
//             setRotation(getRotation()+180);
//         }else {
//             nachricht("Keinen Korrekte Richtung gegeben!");   
//         }
//     }

//     /**
//      * Der Rover gibt durch einen Wahrheitswert (true oder false )zurï¿œck, ob sich auf seiner Position ein Objekt der Klasse Gestein befindet.
//      * Eine entsprechende Meldung erscheint auch auf dem Display.
//      */
//     public boolean gesteinVorhanden()
//     {
//         if(getOneIntersectingObject(Gestein.class)!=null)
//         {
//             nachricht("Gestein gefunden!");
//             return true;

//         }

//         return false;
//     }

//     /**
//      * Der Rover ï¿œberprï¿œft, ob sich in richtung ("rechts", "links", oder "vorne") ein Objekt der Klasse Huegel befindet.
//      * Das Ergebnis wird auf dem Display angezeigt.
//      * Sollte ein anderer Text (String) als "rechts", "links" oder "vorne" ï¿œbergeben werden, dann erscheint eine entsprechende Meldung auf dem Display.
//      */
//     public boolean huegelVorhanden(String richtung)
//     {
//         int rot = getRotation();

//         if (richtung=="vorne" && rot==0 || richtung=="rechts" && rot==270 || richtung=="links" && rot==90)
//         {
//             if(getOneObjectAtOffset(1,0,Huegel.class)!=null && ((Huegel)getOneObjectAtOffset(1,0,Huegel.class)).getSteigung() >30)
//             {
//                 return true;
//             }
//         }

//         if (richtung=="vorne" && rot==180 || richtung=="rechts" && rot==90 || richtung=="links" && rot==270)
//         {
//             if(getOneObjectAtOffset(-1,0,Huegel.class)!=null && ((Huegel)getOneObjectAtOffset(-1,0,Huegel.class)).getSteigung() >30)
//             {
//                 return true;
//             }
//         }

//         if (richtung=="vorne" && rot==90 || richtung=="rechts" && rot==0 || richtung=="links" && rot==180)
//         {
//             if(getOneObjectAtOffset(0,1,Huegel.class)!=null && ((Huegel)getOneObjectAtOffset(0,1,Huegel.class)).getSteigung() >30)
//             {
//                 return true;
//             }

//         }

//         if (richtung=="vorne" && rot==270 || richtung=="rechts" && rot==180 || richtung=="links" && rot==0)
//         {
//             if(getOneObjectAtOffset(0,-1,Huegel.class)!=null && ((Huegel)getOneObjectAtOffset(0,-1,Huegel.class)).getSteigung() >30)
//             {
//                 return true;
//             }

//         }

//         if(richtung!="vorne" && richtung!="links" && richtung!="rechts")
//         {
//             nachricht("Befehl nicht korrekt!");
//         }

//         return false;
//     }

//     /**
//      * Der Rover ermittelt den Wassergehalt des Gesteins auf seiner Position und gibt diesen auf dem Display aus.
//      * Sollte kein Objekt der Klasse Gestein vorhanden sein, dann erscheint eine entsprechende Meldung auf dem Display.
//      */
//     public void analysiereGestein()
//     {
//         if(gesteinVorhanden())
//         {
//             nachricht("Gestein untersucht! Wassergehalt ist " + ((Gestein)getOneIntersectingObject(Gestein.class)).getWassergehalt()+"%.");
//             Greenfoot.delay(1);
//             removeTouching(Gestein.class);
//         }
//         else 
//         {
//             nachricht("Hier ist kein Gestein");
//         }
//     }

//     /**
//      * Der Rover erzeugt ein Objekt der Klasse ï¿œMarkierungï¿œ auf seiner Position.
//      */
//     public void setzeMarke()
//     {
//         getWorld().addObject(new Marke(), getX(), getY());
//     }

//     /**
//      * *Der Rover gibt durch einen Wahrheitswert (true oder false )zurï¿œck, ob sich auf seiner Position ein Objekt der Marke befindet.
//      * Eine entsprechende Meldung erscheint auch auf dem Display.
//      */
//     public boolean markeVorhanden()
//     {
//         if(getOneIntersectingObject(Marke.class)!=null)
//         {
//             return true;
//         }

//         return false;
//     }

//     public void entferneMarke()
//     {
//         if(markeVorhanden())
//         {
//             removeTouching(Marke.class);
//         }
//     }

//     private void nachricht(String pText)
//     {
//         if(anzeige!=null)
//         {
//             anzeige.anzeigen(pText);
//             Greenfoot.delay(1);
//             anzeige.loeschen();
//         }
//     }

//     private void displayAusschalten()
//     {
//         getWorld().removeObject(anzeige);

//     }

//     protected void addedToWorld(World world)
//     {
//         setImage("images/rover.png");
//         world = getWorld();
//         anzeige = new Display();
//         anzeige.setImage("images/nachricht.png");
//         world.addObject(anzeige, 7, 0);
//         if(getY()==0)
//         {
//             setLocation(getX(),1);
//         }
//         anzeige.anzeigen("Ich bin bereit");
//     }

//     class Display extends Actor
//     {
//         GreenfootImage bild; 

//         public Display()
//         {
//             bild = getImage();
//         }

//         public void act() 
//         {

//         }  

//         public void anzeigen(String pText)
//         {
//             loeschen();
//             getImage().drawImage(new GreenfootImage(pText, 25, Color.BLACK, new Color(0, 0, 0, 0)),10,10);

//         }

//         public void loeschen()
//         {
//             getImage().clear();
//             setImage("images/nachricht.png");
//         }

//     }

//     public class Direction  {
//         Direction(int val){
//             this.value = val;
//         }
//         final int value;
//     };
// }

class Testing {

    public void test_function() {
        int rot = getRotation();

        //if (richtung=="vorne" && rot==0 || richtung=="rechts" && rot==270 || richtung=="links" && rot==90)
        //{
            if(getOneObjectAtOffset(1,0,Huegel.class)!=null && ((Huegel)getOneObjectAtOffset(1,0,Huegel.class)).getSteigung() >30)
            {
                return true;
            }
        //}

        //if (richtung=="vorne" && rot==180 || richtung=="rechts" && rot==90 || richtung=="links" && rot==270)
        //{
            // if(getOneObjectAtOffset(-1,0,Huegel.class)!=null && ((Huegel)getOneObjectAtOffset(-1,0,Huegel.class)).getSteigung() >30)
            // {
            //     return true;
            // }
        //}

        // if (richtung=="vorne" && rot==90 || richtung=="rechts" && rot==0 || richtung=="links" && rot==180)
        // {
        //     if(getOneObjectAtOffset(0,1,Huegel.class)!=null && ((Huegel)getOneObjectAtOffset(0,1,Huegel.class)).getSteigung() >30)
        //     {
        //         return true;
        //     }

        // }

        // if (richtung=="vorne" && rot==270 || richtung=="rechts" && rot==180 || richtung=="links" && rot==0)
        // {
        //     if(getOneObjectAtOffset(0,-1,Huegel.class)!=null && ((Huegel)getOneObjectAtOffset(0,-1,Huegel.class)).getSteigung() >30)
        //     {
        //         return true;
        //     }

        // }

        // if(richtung!="vorne" && richtung!="links" && richtung!="rechts")
        // {
        //     nachricht("Befehl nicht korrekt!");
        // }

        // return false;
    }

}