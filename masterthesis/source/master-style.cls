%% Identification part:

\NeedsTeXFormat{LaTeX2e}[1995/12/01]  % Any version, really!

\ProvidesClass{ifimaster}[2020 OsloMet document class]

%% Initial code part:

%% Option declaration part:
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}

\ExecuteOptions{}
\ProcessOptions \relax

%% Base class load part:

\LoadClass[a4paper,12pt,twoside,openright]{report}

%% Adjustments:

%\addtolength{\topmargin}{-2\baselineskip}
%\addtolength{\textheight}{4\baselineskip}
%\addtolength{\evensidemargin}{-5mm}  % Compensate for binding
%\addtolength{\oddsidemargin}{5mm}

\usepackage{geometry}
 \geometry{
 a4paper,
 total={160mm,247mm},
 left=25mm,
 top=25mm,
 }


\pretolerance = 2000
\tolerance = 5000   \hbadness = \tolerance

%% Required packages:

% Times New Roman (12 pt set in LoadClass above)
\RequirePackage[T1]{fontenc}
\RequirePackage{mathptmx}
\renewcommand{\familydefault}{\rmdefault}

%% Document parts:

\newcommand{\frontmatter}{\cleardoublepage \pagenumbering{roman}}
\newcommand{\mainmatter}{\cleardoublepage \pagenumbering{arabic}}
\newcommand{\backmatter}{\cleardoublepage}

\endinput