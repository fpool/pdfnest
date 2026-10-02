# -*- coding: utf-8 -*-
"""PdfNest 多语言数据:de / fr / es(英文默认在 build.py 的 TOOLS)"""

TR = {
"de": {
 "name":"Deutsch",
 "nav_home":"Alle Werkzeuge","nav_privacy":"Datenschutz","nav_about":"Über uns",
 "drop":"Dateien hier ablegen oder klicken zum Auswählen",
 "processing":"Verarbeitung läuft …","done":"Fertig!","download":"Herunterladen","download_zip":"Alle als ZIP herunterladen",
 "no_files":"Bitte zuerst Dateien auswählen.","pages_lbl":"Seiten (leer = alle), z. B. 1-3,5",
 "angle_lbl":"Drehwinkel","start_lbl":"Startnummer",
 "btn":"Verarbeiten","error":"Fehler","bad_type":"Nicht unterstützter Dateityp.",
 "faq_title":"FAQ",
 "privacy_note":"<b>100 % privat:</b> alles läuft lokal in Ihrem Browser. Ihre Dateien werden nie auf einen Server hochgeladen.",
 "privacy":{"title":"Datenschutzerklärung | PdfNest","meta":"Datenschutzerklärung von PdfNest — lokale PDF-Verarbeitung, Cookies und Werbung.",
   "body":"""
  <h1>Datenschutzerklärung</h1>
  <p class="updated">Zuletzt aktualisiert: 2. Oktober 2026</p>
  <p>PdfNest («wir») bietet kostenlose PDF-Werkzeuge, die <b>vollständig in Ihrem Browser</b> laufen. Diese Erklärung erklärt, welche Daten erhoben werden — und welche nicht.</p>
  <h2>1. Ihre Dateien</h2>
  <p><b>Wir sehen Ihre Dateien niemals.</b> Jede Verarbeitung erfolgt lokal auf Ihrem Gerät per JavaScript/WebAssembly. Nichts wird auf einen Server hochgeladen, gespeichert oder protokolliert.</p>
  <h2>2. Serverprotokolle</h2>
  <p>Unser Hosting-Anbieter (Cloudflare) zeichnet automatisch technische Standarddaten auf — IP-Adresse, Browsertyp, URL, Zeitstempel — für Sicherheit und Performance, gemäß der <a href="https://www.cloudflare.com/privacypolicy/">Datenschutzerklärung von Cloudflare</a>.</p>
  <h2>3. Cookies und Werbung</h2>
  <p>Wir planen, Werbung von Google AdSense anzuzeigen. Drittanbieter, einschließlich Google, verwenden Cookies für auf frühere Besuche basierende Werbung. Deaktivierbar über <a href="https://www.google.com/settings/ads">Google Anzeigeneinstellungen</a>; das Blockieren von Cookies beeinträchtigt die Werkzeuge nicht.</p>
  <h2>4. Kontakt</h2>
  <p>Fragen: <b>liuyulong667@gmail.com</b>.</p>"""},
 "about":{"title":"Über PdfNest | PdfNest","meta":"Über PdfNest — kostenlose PDF-Werkzeuge im Browser, ohne Upload.",
   "body":"""
  <h1>Über PdfNest</h1>
  <p>PdfNest ist eine Sammlung schneller, kostenloser PDF-Werkzeuge, die <b>vollständig in Ihrem Browser</b> laufen — Ihre Dokumente werden niemals auf einen Server hochgeladen.</p>
  <h2>Warum PdfNest existiert</h2>
  <p>Die großen Online-PDF-Dienste verlangen, dass Sie private Dokumente auf ihre Server hochladen, nur um Seiten zusammenzuführen oder zu drehen. Wir finden das rückwärts — deshalb passiert bei PdfNest alles lokal.</p>
  <h2>Prinzipien</h2>
  <ul><li><b>Lokal als Standard.</b> Kein Upload-Schritt, weil es ihn nie gab.</li>
  <li><b>Kostenlos heißt kostenlos.</b> Keine Anmeldung, kein Wasserzeichen, keine Limits.</li>
  <li><b>Werkzeug zuerst.</b> Eine Aufgabe, in Sekunden erledigt.</li></ul>
  <h2>Kontakt</h2>
  <p>Feedback: <b>liuyulong667@gmail.com</b>.</p>"""},
 "tools":{
  "merge":{"title":"PDF zusammenführen — Kostenlos, ohne Upload | PdfNest","h1":"PDF zusammenführen",
   "meta":"Mehrere PDF-Dateien kostenlos online zusammenführen. 100 % privat — Dateien verlassen nie Ihren Browser. Keine Anmeldung, kein Wasserzeichen.",
   "intro":"Zwei oder mehr PDF-Dateien in der gewählten Reihenfolge zu einem Dokument zusammenführen.",
   "faq":[("Ist das wirklich privat?","Ja — die Zusammenführung läuft per JavaScript in Ihrem Browser. Ihre Dateien werden nie hochgeladen."),
     ("Wie viele Dateien kann ich zusammenführen?","Praktisch unbegrenzt — begrenzt nur durch den Speicher Ihres Geräts."),
     ("Bleibt die Qualität erhalten?","Ja — Seiten werden ohne Neukomprimierung kopiert, Qualität und Text bleiben erhalten.")]},
  "split":{"title":"PDF aufteilen — Jede Seite als eigene Datei | PdfNest","h1":"PDF aufteilen",
   "meta":"PDF kostenlos online aufteilen — jede Seite wird zu einer eigenen Datei, Download als ZIP. Privat, ohne Upload.",
   "intro":"Ein PDF in einzelne Seiten aufteilen — jede Seite wird zu einer eigenen PDF-Datei, alles als ZIP gepackt.",
   "faq":[("Kann ich Seitenbereiche angeben?","Ja — im Seitenfeld z. B. 1-3,5 eintragen; nur diese Seiten werden aufgeteilt."),
     ("Wie heißen die Ausgabedateien?","Originalname mit Seitennummer, z. B. dokument_p2.pdf."),
     ("Ist das wirklich privat?","Ja — alles läuft in Ihrem Browser, nichts wird hochgeladen.")]},
  "rotate":{"title":"PDF-Seiten drehen — Kostenlos, ohne Upload | PdfNest","h1":"PDF-Seiten drehen",
   "meta":"PDF-Seiten online kostenlos um 90/180/270 Grad drehen. Privat — Dateien verlassen nie Ihren Browser.",
   "intro":"Bestimmte oder alle Seiten eines PDFs um 90, 180 oder 270 Grad drehen.",
   "faq":[("Kann ich nur einzelne Seiten drehen?","Ja — Seitenfeld leer lassen für alle Seiten, oder z. B. 1-3,7 eintragen."),
     ("Ist die Drehung dauerhaft?","Ja — die Seiten werden im neuen PDF physisch gedreht gespeichert."),
     ("Bleiben Text und Qualität erhalten?","Ja — nur die Seitenansicht wird gedreht, Inhalt bleibt unberührt.")]},
  "delete-pages":{"title":"PDF-Seiten löschen — Kostenlos, ohne Upload | PdfNest","h1":"PDF-Seiten löschen",
   "meta":"Seiten aus einem PDF kostenlos online löschen. Privat — Dateien verlassen nie Ihren Browser.",
   "intro":"Ungewollte Seiten entfernen — der Rest bleibt als sauberes PDF erhalten.",
   "faq":[("Wie gebe ich zu löschende Seiten an?","Einzeln oder Bereiche, z. B. 2,5-7. Diese Seiten werden entfernt, alle anderen bleiben."),
     ("Kann ich das rückgängig machen?","Laden Sie die Originaldatei einfach erneut — Ihre Originale bleiben unberührt, da alles lokal passiert."),
     ("Bleiben Lesezeichen und Text erhalten?","Ja — der Rest des Dokuments bleibt unverändert.")]},
  "images-to-pdf":{"title":"Bilder zu PDF — JPG/PNG kostenlos umwandeln | PdfNest","h1":"Bilder zu PDF",
   "meta":"JPG- und PNG-Bilder kostenlos online in ein PDF umwandeln. Privat — Bilder verlassen nie Ihren Browser.",
   "intro":"Mehrere Bilder (JPG/PNG) in ein PDF umwandeln — jedes Bild wird eine Seite in der gewählten Reihenfolge.",
   "faq":[("Welche Formate werden unterstützt?","JPG/JPEG und PNG. Jedes Bild wird eine vollseitige PDF-Seite in Bildgröße."),
     ("Bleibt die Bildqualität erhalten?","Ja — Bilder werden ohne Neukomprimierung eingebettet."),
     ("Kann ich die Reihenfolge ändern?","Die Dateien werden in Auswahlliste-Reihenfolge verarbeitet — wählen Sie sie in der gewünschten Reihenfolge aus.")]},
  "pdf-to-images":{"title":"PDF zu Bilder — Als JPG exportieren | PdfNest","h1":"PDF zu Bilder",
   "meta":"PDF-Seiten kostenlos online als JPG-Bilder exportieren. Privat — Dateien verlassen nie Ihren Browser.",
   "intro":"Jede PDF-Seite als JPG-Bild exportieren — ideal für Vorschauen, Präsentationen oder Messaging-Apps.",
   "faq":[("Welche Auflösung haben die Bilder?","Seiten werden in hoher Qualität gerendert (2-fache Skalierung) — scharf für Bildschirm und Druck."),
     ("Alle Seiten oder bestimmte?","Standardmäßig alle; im Seitenfeld können Sie Bereiche angeben, z. B. 1-5."),
     ("Wie erhalte ich alle Bilder?","Als einzelne JPGs oder alle zusammen als ZIP — beides mit einem Klick.")]},
  "extract-text":{"title":"Text aus PDF extrahieren — Kostenlos | PdfNest","h1":"Text aus PDF extrahieren",
   "meta":"Text aus PDF-Dateien kostenlos online extrahieren. Privat — Dateien verlassen nie Ihren Browser.",
   "intro":"Den gesamten Text eines PDFs extrahieren — mit Seitenmarken, bereit zum Kopieren oder als TXT-Datei.",
   "faq":[("Funktioniert das bei gescannten PDFs?","Nein — gescannte Seiten sind Bilder ohne Textschicht; dafür wäre OCR nötig (nicht in diesem Werkzeug)."),
     ("Wird das Layout erhalten?","Der Text wird pro Seite in Lesereihenfolge extrahiert — komplexes Layout wird vereinfacht."),
     ("Wie speichere ich den Text?","Als TXT herunterladen oder einfach markieren und kopieren.")]},
  "page-numbers":{"title":"PDF-Seitenzahlen hinzufügen — Kostenlos | PdfNest","h1":"Seitenzahlen hinzufügen",
   "meta":"PDF-Seitenzahlen kostenlos online hinzufügen — Position und Startnummer wählbar. Privat, ohne Upload.",
   "intro":"Seitenzahlen zu einem PDF hinzufügen — Position und Startnummer frei wählbar.",
   "faq":[("Kann ich bei einer anderen Zahl starten?","Ja — Startnummer frei wählbar, z. B. 1 bei einem Deckblatt ohne Nummer."),
     ("Wo erscheint die Zahl?","Standardmäßig unten mittig auf jeder Seite."),
     ("Bleibt der Rest unverändert?","Ja — nur die Zahlen werden hinzugefügt, Inhalt und Layout bleiben unberührt.")]},
 }
},
"fr": {
 "name":"Français",
 "nav_home":"Tous les outils","nav_privacy":"Confidentialité","nav_about":"À propos",
 "drop":"Déposez vos fichiers ici ou cliquez pour choisir",
 "processing":"Traitement en cours …","done":"Terminé !","download":"Télécharger","download_zip":"Tout télécharger en ZIP",
 "no_files":"Choisissez d'abord des fichiers.","pages_lbl":"Pages (vide = toutes), ex. 1-3,5",
 "angle_lbl":"Angle de rotation","start_lbl":"Numéro de départ",
 "btn":"Traiter","error":"Erreur","bad_type":"Type de fichier non pris en charge.",
 "faq_title":"FAQ",
 "privacy_note":"<b>100 % privé :</b> tout s'exécute localement dans votre navigateur. Vos fichiers ne sont jamais envoyés à un serveur.",
 "privacy":{"title":"Politique de confidentialité | PdfNest","meta":"Politique de confidentialité de PdfNest — traitement local des PDF, cookies et publicité.",
   "body":"""
  <h1>Politique de confidentialité</h1>
  <p class="updated">Dernière mise à jour : 2 octobre 2026</p>
  <p>PdfNest (« nous ») propose des outils PDF gratuits qui fonctionnent <b>entièrement dans votre navigateur</b>. Cette politique explique quelles données sont — et ne sont pas — collectées.</p>
  <h2>1. Vos fichiers</h2>
  <p><b>Nous ne voyons jamais vos fichiers.</b> Tout le traitement s'effectue localement sur votre appareil en JavaScript/WebAssembly. Rien n'est téléversé, stocké ou enregistré.</p>
  <h2>2. Journaux serveur</h2>
  <p>Notre hébergeur (Cloudflare) enregistre automatiquement les données techniques standard — IP, type de navigateur, URL, horodatage — à des fins de sécurité et de performance, conformément à la <a href="https://www.cloudflare.com/privacypolicy/">politique de confidentialité de Cloudflare</a>.</p>
  <h2>3. Cookies et publicité</h2>
  <p>Nous prévoyons d'afficher de la publicité servie par Google AdSense. Des tiers, dont Google, utilisent des cookies pour des annonces basées sur les visites précédentes. Désactivables via <a href="https://www.google.com/settings/ads">les paramètres des annonces Google</a> ; bloquer les cookies n'affecte pas les outils.</p>
  <h2>4. Contact</h2>
  <p>Questions : <b>liuyulong667@gmail.com</b>.</p>"""},
 "about":{"title":"À propos de PdfNest | PdfNest","meta":"À propos de PdfNest — des outils PDF gratuits dans le navigateur, sans téléversement.",
   "body":"""
  <h1>À propos de PdfNest</h1>
  <p>PdfNest est une collection d'outils PDF rapides et gratuits qui fonctionnent <b>entièrement dans votre navigateur</b> — vos documents ne sont jamais téléversés sur un serveur.</p>
  <h2>Pourquoi PdfNest existe</h2>
  <p>Les grands services PDF en ligne vous demandent de téléverser des documents privés sur leurs serveurs juste pour fusionner ou faire pivoter des pages. Nous trouvons cela absurde — chez PdfNest, tout se passe localement.</p>
  <h2>Principes</h2>
  <ul><li><b>Local par défaut.</b> Aucune étape de téléversement, parce qu'elle n'a jamais existé.</li>
  <li><b>Gratuit veut dire gratuit.</b> Sans inscription, sans filigrane, sans limite.</li>
  <li><b>L'outil d'abord.</b> Une tâche, réglée en quelques secondes.</li></ul>
  <h2>Contact</h2>
  <p>Retours : <b>liuyulong667@gmail.com</b>.</p>"""},
 "tools":{
  "merge":{"title":"Fusionner des PDF — Gratuit, sans téléversement | PdfNest","h1":"Fusionner des PDF",
   "meta":"Fusionnez plusieurs PDF en ligne gratuitement. 100 % privé — les fichiers ne quittent jamais votre navigateur. Sans inscription ni filigrane.",
   "intro":"Combiner deux PDF ou plus en un seul document, dans l'ordre choisi.",
   "faq":[("Est-ce vraiment privé ?","Oui — la fusion s'exécute en JavaScript dans votre navigateur. Vos fichiers ne sont jamais téléversés."),
     ("Combien de fichiers puis-je fusionner ?","Pratiquement illimité — limité seulement par la mémoire de votre appareil."),
     ("La qualité est-elle préservée ?","Oui — les pages sont copiées sans recompression : texte et qualité intacts.")]},
  "split":{"title":"Diviser un PDF — Chaque page en un fichier | PdfNest","h1":"Diviser un PDF",
   "meta":"Divisez un PDF en ligne gratuitement — chaque page devient un fichier, téléchargement en ZIP. Privé, sans téléversement.",
   "intro":"Diviser un PDF en pages individuelles — chaque page devient un fichier PDF, le tout regroupé en ZIP.",
   "faq":[("Puis-je préciser des pages ?","Oui — saisissez par ex. 1-3,5 dans le champ pages ; seules ces pages seront divisées."),
     ("Comment s'appellent les fichiers ?","Nom d'origine avec numéro de page, ex. document_p2.pdf."),
     ("Est-ce vraiment privé ?","Oui — tout se passe dans votre navigateur, rien n'est téléversé.")]},
  "rotate":{"title":"Faire pivoter des pages PDF — Gratuit | PdfNest","h1":"Faire pivoter des pages PDF",
   "meta":"Faites pivoter des pages PDF en ligne de 90/180/270 degrés. Privé — les fichiers ne quittent jamais votre navigateur.",
   "intro":"Faire pivoter certaines ou toutes les pages d'un PDF de 90, 180 ou 270 degrés.",
   "faq":[("Puis-je faire pivoter seulement certaines pages ?","Oui — champ pages vide pour toutes, ou par ex. 1-3,7."),
     ("La rotation est-elle permanente ?","Oui — les pages sont physiquement enregistrées pivotées dans le nouveau PDF."),
     ("Le texte et la qualité sont-ils conservés ?","Oui — seule la vue de la page pivote, le contenu reste intact.")]},
  "delete-pages":{"title":"Supprimer des pages PDF — Gratuit | PdfNest","h1":"Supprimer des pages PDF",
   "meta":"Supprimez des pages d'un PDF en ligne gratuitement. Privé — les fichiers ne quittent jamais votre navigateur.",
   "intro":"Retirer les pages indésirables — le reste reste un PDF propre.",
   "faq":[("Comment indiquer les pages à supprimer ?","Individuellement ou par plages, ex. 2,5-7. Ces pages sont retirées, les autres conservées."),
     ("Puis-je annuler ?","Rechargez simplement le fichier d'origine — vos originaux restent intacts, tout se passe localement."),
     ("Signets et texte sont-ils conservés ?","Oui — le reste du document reste inchangé.")]},
  "images-to-pdf":{"title":"Images vers PDF — JPG/PNG gratuit | PdfNest","h1":"Images vers PDF",
   "meta":"Convertissez gratuitement des images JPG/PNG en un PDF en ligne. Privé — les images ne quittent jamais votre navigateur.",
   "intro":"Convertir plusieurs images (JPG/PNG) en un PDF — chaque image devient une page, dans l'ordre choisi.",
   "faq":[("Quels formats sont pris en charge ?","JPG/JPEG et PNG. Chaque image devient une page pleine aux dimensions de l'image."),
     ("La qualité est-elle préservée ?","Oui — les images sont intégrées sans recompression."),
     ("Puis-je changer l'ordre ?","Les fichiers sont traités dans l'ordre de la liste — sélectionnez-les dans l'ordre souhaité.")]},
  "pdf-to-images":{"title":"PDF vers images — Exporter en JPG | PdfNest","h1":"PDF vers images",
   "meta":"Exportez les pages d'un PDF en images JPG en ligne gratuitement. Privé — les fichiers ne quittent jamais votre navigateur.",
   "intro":"Exporter chaque page d'un PDF en image JPG — idéal pour aperçus, présentations ou applications de messagerie.",
   "faq":[("Quelle est la résolution des images ?","Les pages sont rendues en haute qualité (échelle 2x) — nettes pour écran et impression."),
     ("Toutes les pages ou certaines ?","Toutes par défaut ; précisez des plages dans le champ pages, ex. 1-5."),
     ("Comment récupérer toutes les images ?","En JPG individuels ou tout en ZIP — les deux en un clic.")]},
  "extract-text":{"title":"Extraire le texte d'un PDF — Gratuit | PdfNest","h1":"Extraire le texte d'un PDF",
   "meta":"Extrayez le texte de fichiers PDF en ligne gratuitement. Privé — les fichiers ne quittent jamais votre navigateur.",
   "intro":"Extraire tout le texte d'un PDF — avec des marqueurs de page, prêt à copier ou en fichier TXT.",
   "faq":[("Fonctionne-t-il sur les PDF scannés ?","Non — les pages scannées sont des images sans couche de texte ; cela nécessiterait une OCR (absente de cet outil)."),
     ("La mise en page est-elle conservée ?","Le texte est extrait par page dans l'ordre de lecture — les mises en page complexes sont simplifiées."),
     ("Comment enregistrer le texte ?","Téléchargez en TXT ou sélectionnez et copiez simplement.")]},
  "page-numbers":{"title":"Ajouter des numéros de page — Gratuit | PdfNest","h1":"Ajouter des numéros de page",
   "meta":"Ajoutez des numéros de page à un PDF en ligne — position et numéro de départ au choix. Privé, sans téléversement.",
   "intro":"Ajouter des numéros de page à un PDF — position et numéro de départ au choix.",
   "faq":[("Puis-je commencer à un autre numéro ?","Oui — numéro de départ libre, ex. 1 sur une couverture non numérotée."),
     ("Où apparaît le numéro ?","Par défaut en bas au centre de chaque page."),
     ("Le reste est-il inchangé ?","Oui — seuls les numéros sont ajoutés, contenu et mise en page intacts.")]},
 }
},
"es": {
 "name":"Español",
 "nav_home":"Todas las herramientas","nav_privacy":"Privacidad","nav_about":"Acerca de",
 "drop":"Arrastra tus archivos aquí o haz clic para elegir",
 "processing":"Procesando …","done":"¡Listo!","download":"Descargar","download_zip":"Descargar todo en ZIP",
 "no_files":"Primero elige algunos archivos.","pages_lbl":"Páginas (vacío = todas), ej. 1-3,5",
 "angle_lbl":"Ángulo de rotación","start_lbl":"Número inicial",
 "btn":"Procesar","error":"Error","bad_type":"Tipo de archivo no compatible.",
 "faq_title":"Preguntas frecuentes",
 "privacy_note":"<b>100 % privado:</b> todo se ejecuta localmente en tu navegador. Tus archivos nunca se suben a ningún servidor.",
 "privacy":{"title":"Política de privacidad | PdfNest","meta":"Política de privacidad de PdfNest — procesamiento local de PDF, cookies y publicidad.",
   "body":"""
  <h1>Política de privacidad</h1>
  <p class="updated">Última actualización: 2 de octubre de 2026</p>
  <p>PdfNest («nosotros») ofrece herramientas PDF gratuitas que funcionan <b>enteramente en tu navegador</b>. Esta política explica qué datos se recopilan — y cuáles no.</p>
  <h2>1. Tus archivos</h2>
  <p><b>Nunca vemos tus archivos.</b> Todo el procesamiento ocurre localmente en tu dispositivo con JavaScript/WebAssembly. Nada se sube, guarda ni registra.</p>
  <h2>2. Registros del servidor</h2>
  <p>Nuestro proveedor de alojamiento (Cloudflare) registra automáticamente datos técnicos estándar — IP, tipo de navegador, URL, fecha — con fines de seguridad y rendimiento, conforme a la <a href="https://www.cloudflare.com/privacypolicy/">política de privacidad de Cloudflare</a>.</p>
  <h2>3. Cookies y publicidad</h2>
  <p>Planeamos mostrar publicidad servida por Google AdSense. Terceros, incluido Google, usan cookies para anuncios basados en visitas previas. Desactivables en <a href="https://www.google.com/settings/ads">Configuración de anuncios de Google</a>; bloquear cookies no afecta las herramientas.</p>
  <h2>4. Contacto</h2>
  <p>Preguntas: <b>liuyulong667@gmail.com</b>.</p>"""},
 "about":{"title":"Acerca de PdfNest | PdfNest","meta":"Acerca de PdfNest — herramientas PDF gratuitas en el navegador, sin subidas.",
   "body":"""
  <h1>Acerca de PdfNest</h1>
  <p>PdfNest es una colección de herramientas PDF rápidas y gratuitas que funcionan <b>enteramente en tu navegador</b> — tus documentos nunca se suben a un servidor.</p>
  <h2>Por qué existe PdfNest</h2>
  <p>Los grandes servicios PDF en línea te hacen subir documentos privados a sus servidores solo para combinar o rotar páginas. Nos parece al revés — en PdfNest todo ocurre localmente.</p>
  <h2>Principios</h2>
  <ul><li><b>Local por defecto.</b> No hay paso de subida que eliminar, porque nunca existió.</li>
  <li><b>Gratis significa gratis.</b> Sin registro, sin marca de agua, sin límites.</li>
  <li><b>La herramienta primero.</b> Una tarea, resuelta en segundos.</li></ul>
  <h2>Contacto</h2>
  <p>Comentarios: <b>liuyulong667@gmail.com</b>.</p>"""},
 "tools":{
  "merge":{"title":"Combinar PDF — Gratis, sin subidas | PdfNest","h1":"Combinar PDF",
   "meta":"Combina varios PDF en línea gratis. 100 % privado — los archivos nunca salen de tu navegador. Sin registro ni marca de agua.",
   "intro":"Unir dos o más archivos PDF en un solo documento, en el orden que elijas.",
   "faq":[("¿De verdad es privado?","Sí — la combinación se ejecuta en JavaScript dentro de tu navegador. Tus archivos nunca se suben."),
     ("¿Cuántos archivos puedo combinar?","Prácticamente ilimitados — solo lo limita la memoria de tu dispositivo."),
     ("¿Se mantiene la calidad?","Sí — las páginas se copian sin recomprimir: texto y calidad intactos.")]},
  "split":{"title":"Dividir PDF — Cada página en un archivo | PdfNest","h1":"Dividir PDF",
   "meta":"Divide un PDF en línea gratis — cada página se convierte en un archivo, descarga en ZIP. Privado, sin subidas.",
   "intro":"Dividir un PDF en páginas individuales — cada página se convierte en un archivo PDF, todo empaquetado en ZIP.",
   "faq":[("¿Puedo indicar páginas?","Sí — escribe p. ej. 1-3,5 en el campo páginas; solo esas se dividirán."),
     ("¿Cómo se llaman los archivos?","Nombre original con número de página, ej. documento_p2.pdf."),
     ("¿De verdad es privado?","Sí — todo ocurre en tu navegador, nada se sube.")]},
  "rotate":{"title":"Rotar páginas PDF — Gratis | PdfNest","h1":"Rotar páginas PDF",
   "meta":"Rota páginas PDF en línea 90/180/270 grados gratis. Privado — los archivos nunca salen de tu navegador.",
   "intro":"Rotar páginas específicas o todas las páginas de un PDF 90, 180 o 270 grados.",
   "faq":[("¿Puedo rotar solo algunas páginas?","Sí — deja el campo de páginas vacío para todas, o escribe p. ej. 1-3,7."),
     ("¿La rotación es permanente?","Sí — las páginas se guardan físicamente rotadas en el nuevo PDF."),
     ("¿Se conservan texto y calidad?","Sí — solo gira la vista de la página, el contenido queda intacto.")]},
  "delete-pages":{"title":"Eliminar páginas PDF — Gratis | PdfNest","h1":"Eliminar páginas PDF",
   "meta":"Elimina páginas de un PDF en línea gratis. Privado — los archivos nunca salen de tu navegador.",
   "intro":"Quitar las páginas que no quieres — el resto queda como un PDF limpio.",
   "faq":[("¿Cómo indico las páginas a eliminar?","Individualmente o por rangos, ej. 2,5-7. Esas páginas se eliminan, las demás se conservan."),
     ("¿Puedo deshacerlo?","Vuelve a cargar el archivo original — tus originales quedan intactos, todo ocurre localmente."),
     ("¿Se conservan marcadores y texto?","Sí — el resto del documento queda sin cambios.")]},
  "images-to-pdf":{"title":"Imágenes a PDF — Convertir JPG/PNG gratis | PdfNest","h1":"Imágenes a PDF",
   "meta":"Convierte imágenes JPG/PNG a un PDF en línea gratis. Privado — las imágenes nunca salen de tu navegador.",
   "intro":"Convertir varias imágenes (JPG/PNG) en un PDF — cada imagen se convierte en una página, en el orden elegido.",
   "faq":[("¿Qué formatos admite?","JPG/JPEG y PNG. Cada imagen se convierte en una página completa del tamaño de la imagen."),
     ("¿Se mantiene la calidad?","Sí — las imágenes se incrustan sin recomprimir."),
     ("¿Puedo cambiar el orden?","Los archivos se procesan en el orden de la lista — selecciónalos en el orden deseado.")]},
  "pdf-to-images":{"title":"PDF a imágenes — Exportar como JPG | PdfNest","h1":"PDF a imágenes",
   "meta":"Exporta las páginas de un PDF como imágenes JPG en línea gratis. Privado — los archivos nunca salen de tu navegador.",
   "intro":"Exportar cada página de un PDF como imagen JPG — ideal para vistas previas, presentaciones o apps de mensajería.",
   "faq":[("¿Qué resolución tienen las imágenes?","Las páginas se renderizan en alta calidad (escala 2x) — nítidas para pantalla e impresión."),
     ("¿Todas las páginas o algunas?","Todas por defecto; indica rangos en el campo páginas, ej. 1-5."),
     ("¿Cómo obtengo todas las imágenes?","Como JPG individuales o todas en un ZIP — ambos con un clic.")]},
  "extract-text":{"title":"Extraer texto de un PDF — Gratis | PdfNest","h1":"Extraer texto de un PDF",
   "meta":"Extrae el texto de archivos PDF en línea gratis. Privado — los archivos nunca salen de tu navegador.",
   "intro":"Extraer todo el texto de un PDF — con marcas de página, listo para copiar o como archivo TXT.",
   "faq":[("¿Funciona con PDF escaneados?","No — las páginas escaneadas son imágenes sin capa de texto; eso requeriría OCR (no incluido en esta herramienta)."),
     ("¿Se conserva el diseño?","El texto se extrae por página en orden de lectura — los diseños complejos se simplifican."),
     ("¿Cómo guardo el texto?","Descárgalo como TXT o simplemente selecciónalo y cópialo.")]},
  "page-numbers":{"title":"Añadir números de página — Gratis | PdfNest","h1":"Añadir números de página",
   "meta":"Añade números de página a un PDF en línea — posición y número inicial a elegir. Privado, sin subidas.",
   "intro":"Añadir números de página a un PDF — posición y número inicial a elegir.",
   "faq":[("¿Puedo empezar en otro número?","Sí — número inicial libre, ej. 1 en una portada sin numerar."),
     ("¿Dónde aparece el número?","Por defecto abajo al centro de cada página."),
     ("¿El resto queda igual?","Sí — solo se añaden los números, contenido y diseño intactos.")]},
 }
},
}
