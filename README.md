# Reports for the advanced lab course in the physics master degree

**Description**

From [Moodle](https://moodle.tu-dortmund.de/):
> The advanced physics lab course serves to strengthen the knowledge obtained in the beginner lab courses.

The structure of this project as well as the employed methods are based on the
[Toolbox-Workshop](https://toolbox.pep-dortmund.org/notes/) held by
[PeP et al. e.V.](https://pep-dortmund.org/) For reference, the
[Fachschaft](https://fachschaft-physik.tu-dortmund.de/wordpress/studium/praktikum/altprotokolle-fp/)
provides previous lab reports.

**Authors**

Fritz Ali Agildere ([fritz.agildere@udo.edu](mailto:fritz.agildere@udo.edu)) und
Jan Lucca Viola ([janlucca.viola@udo.edu](mailto:janlucca.viola@udo.edu))

**Structure**

The reports are created as a PDF file via the `make` command. General configuration is done in the main directory and adopted in the subdirectories by default.
Individual experiments consist of the directories `build` for all generated files as well as `content`  which represents the structure of the report:

1. Objective
2. Theory
3. Procedure
4. Results
5. Discussion

For graphical presentation and the automated generation of results, `python` scripts with the required packages are used. Documents are compiled using `lualatex`.

The project *Advanced Laboratory* is compatible with GNU/Linux.
