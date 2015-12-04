# Interface Utilisateur Tangible

## Naissance [@shaer2010tangible]

En 1993, une édition spéciale des communications d'ACM titre "Back to the Real World" [@wellner1993back] et affirme que les ordinateurs et la réalité virtuelle éloignent les hommes de leur "environnement naturel". Il insinue qu'au lieu de forcer les utilisateurs à entrer dans un monde virtuelle, les ordinateurs devrait être utilisés pour augmenter et enrichir le monde réel avec des fonctionnalités numériques. 

En 1995, Fitzmaurice et al. [@fitzmaurice1995bricks] introduit la notion de "Graspable Interface", où des objets physiques sont saisissables par l'utilisateur afin de manipuler des objets numériques.

En 1997, Ishii et ses étudiants [@ishii1997tangible] présentent les "Tangible bits". Leur vision est centrée sur la transformation du monde physique en une interface, en connectant les objets et surfaces avec le monde numérique.

En 2001, Ullmer et Ishii définissent les Interfaces Utilisateurs Tangibles comme étant des systèmes qui utilisent des objets physiques pour représenter et manipuler les données numériques. En s'inspirant du célèbre modèle MVC (Model, View, Control), Ulmer et Ishii ont également suggérés un modèle d'interaction appelé MCRit qui est une abréviation pour Model-Control-Représentation (intangible et tangible). Alors que le modèle MVC fait la distinction entre la représentation graphique (i.e. une sortie) et le contrôle (i.e. une entrée), le modèle MCRit met en avant le fait que les entrées et les sorties dans les Interfaces Utilisateurs Tangibles sont confondus par une représentation et un contrôle des données directes dans le monde physique.

![](images/mcritmodel.jpg)
<h4 style="text-align:center">MCRit Model [@ullmer2000emerging]</h4>

## Avantages

### La Collaboration

Depuis le début, Les Interfaces Utilisateurs Tangibles cherchent à favoriser le dialogue entre les experts (e.g., architecte) et les parties concernées (e.g., futurs habitants du bâtiment) et à supporter l'apprentissage collaboratif.

### L'applicabilité

Les Interfaces Utilisateurs Tangibles peuvent exister dans notre monde et se placer dans des contextes précis. En effet, la sémantique d'interaction avec l'interface tangible peut changer en fonction du contexte dans lequel elle se trouve.

### La réflexion tangible

Notre corps et les objets physiques avec les quelles nous interagissons jouent un rôle central dans le façonnage de notre compréhension du monde [@klemmer2006bodies], [@turkle2011evocative]. Les interfaces Utilisateurs Tangibles permette de renforcer cette connexion entre le corps et la cognition en facilitant la réflexion tangible - Réflexion par le biais d'actions, de manipulations physiques, et de représentation tangible.

### La gestuelle

Alors que les gestes sont typiquement considérés comme un moyen de communication, plusieurs études illustrent le fait que les gestes jouent un rôle dans l'allégement de la charge cognitive que se soit celle des enfants ou celle des adultes [@alibali2000gesture]. En fournissant aux utilisateurs de multiples points d'accès au système et en maintenant leur mobilité physique.

### Les Actions épistémiques et accessoires de réflexion

Plusieurs études ont démontrés que les artefacts physiques supportent la cognition en servant d' "accessoires de réflexion" et de mémoire externes. On distingue les actions pragmatiques qui ont des conséquences fonctionnelles et donc contribuent à l'accomplissement d'un but et les actions épistémiques qui n'ont pas de conséquences fonctionnelles mais plutôt changent la nature de la tache mentale [@kirsh1994distinguishing]. Les actions épistémiques aide à explorer des options, à garder la trace des décisions précédemment prissent, et aide à la mémorisation. Des actions comme pointer un objet, le réarranger, le tourner, le cacher, etc. Les Interfaces Utilisateurs Tangibles cherchent à rendre les actions épistémiques plus facile qu'avec une Interface Utilisateur traditionnelle.

### La représentation tangible

Il a été démontré que les représentations externes d'informations sont des composantes intrinsèques à beaucoup de tache cognitives car elles guides, contraignent, et même déterminent le comportement cognitif [@zhang1997nature]. Ils existent de nombreux domaines des Interfaces Utilisateurs Tangibles où l'ont utilisent des objets physiques en tant que représentation externes d'informations numériques : architecture, économie, musique, biologie, création, chimie, etc.

### Le multiplexage de l'espace et la spontanéité de l'interaction.

Dans les interfaces tangibles qui utilisent plusieurs objets d'interaction, l'entrée de l'information est spatialisée. Les différents objets représentent différentes fonctions ou données. Ceci permet au concepteur du système de prendre avantage de la forme, la taille, et de la position du contrôleur physique pour accroître ses fonctionnalités et réduire la complexité de l'interaction. De plus, Ceci permet un mapping persistante, comparé à une GUI traditionnelle, où chaque clique de souris peut provoquer l'appel d'une fonction ou la sélection d'un objet non souhaité. Plusieurs interacteurs spécifiques permettent des actions parallèles. Au contraire d'une interface classique où l'utilisateur doit séquentiellement effectuer les actions les unes après les autres.

### Une incarnation forte de la données qui créer de l'affordance et de l'iconicité

Utiliser plusieurs interacteurs permet de créer des entrées qui ne sont ni génériques, ni abstraites mais spécifiques, dédié par leur forme et leur apparence à une fonctionnalité particulière. L'apparence d'un objet peut directement indiquer sa signification, sa fonctionnalité associée mais également comment interagir avec lui par l'utilisation de l'affordance.

## Limitations

### La flexibilité et le risque de perdre les objets physiques.

Des applications réussites des Interfaces Utilisateurs Tangibles pour de petits problèmes ou pour de petits échantillons de données sont rarement applicables à des problèmes plus complexes incluant beaucoup de paramètres et des échantillons de données plus grands. Il y a plusieurs raisons à ce problème :
L'espace occupé par les objets physiques de l'Interface Tangible. En effet combien d'objets peuvent être supporter par une surface interactive avant que cette dernière devienne inutilisable. Si cette surface venait à grandir, il serait beaucoup plus difficile pour un utilisateur d'accéder et déplacer les objets car il devrait se déplacer, voir voler, sur la surface. Un autre problème est la forme extrême de manipulation donnée par les Interfaces Utilisateurs Tangibles aux données, cette dernière ne permet pas à l'utilisateur d'accéder et de modifier des variables internes à la données comme le ferai simplement une ligne de commande dans une interface traditionnelle [@bellotti2002making].

### La polyvalence et la malléabilité

Les données numériques sont malléables, facile à créer, modifier, répliquer, et à distribuer, les objets physiques quand à eux sont rigides et statiques [@poupyrev2007actuation]. Un interface utilisateur graphique peut etre utilisé pour effectuer une variété de tâches tels que l'écriture de document, chatter avec des amis, et jouer de la musique. Cependant, une Interface Utilisateur Tangible est typiquement conçue pour un panel de tâche limité. De plus, une interface utilisateur graphique permet à l'utilisateur de changer de vue ou de représentations (e.g., de la vue carte à la vue satellite). Avec une Interface Utilisateur Tangible un tel changement est difficile du fait que la représentation tangible est déja choisie.

### La fatigue

Les effets de la taille et du poids des objets tangibles ne doit pas être sous-estimé. Le design physique de l'objet ne devrait pas seulement considéré l'affordance en terme d'actions que l'utilisateur est invité à effectuer par la forme physique de l'objet, mais aussi l'ergonomie et la durée potentielle d'utilisation de l'objet tangible.



## Références
