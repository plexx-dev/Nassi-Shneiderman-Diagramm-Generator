public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}

private void S66Nr3(int anzahlZeilen)
{
    if(anzahlZeilen < 3) {
        nachricht("Ich muss mindestens drei Zeilen fahren! :(");
        return;
    }
    fahreZeileDreheHoch();
    for(int i = 1; i < anzahlZeilen-1; i++) {
        fahreZeileDreheRunter(true);
    }
    fahreZeileDreheRunter(false);
}
public void act()
{
    S66Nr3(7);
}

private void fahreUmHuegel(String richtung)
{
    String pri;
    String sec;
    if(richtung.equals("Hoch")) {
        pri = "links";
        sec = "rechts";
    } else {
        if (richtung.equals("Runter")){
            pri = "rechts";
            sec = "links";
        } else {
            nachricht("JUNGE DU SPAST!");
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

private void fahreBisHuegel()
{
    while(!huegelVorhanden("vorne"))
    {
        fahre();
    }
}

private void fahreZeileDreheHoch()
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

private void fahreZeileDreheRunter(boolean geheInNächsteZeile)
{
    fahreBisHuegel();
    fahreUmHuegel("Runter");
    fahreBisHuegel();
    drehe("um");

    fahreBisHuegel();
    fahreUmHuegel("Hoch");
    fahreBisHuegel();
    if(geheInNächsteZeile) {
        drehe("rechts");
        fahre();
        drehe("rechts");
    } else {
        drehe("um");
    }
}