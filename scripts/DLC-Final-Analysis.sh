#!/bin/bash

jobs=/projects/b1090/Users/sajiv/DLC-DATA/jobs

if [ ! -e $jobs ]; then mkdir $jobs; echo "making output directory"; fi

for i in {2..18};
do

echo -e "import deeplabcut" >> $jobs/Analysis_Acq_${i}.py
echo -e "deeplabcut.analyze_videos('/projects/b1090/Users/sajiv/DLC-DATA/Explore-Sajiv-2023-08-18/config.yaml',['/projects/b1090/Users/sajiv/DLC-DATA/RatVideos/NOR10_Acq_R${i}.mp4'], save_as_csv=True, videotype='.mp4')" >> $jobs/Analysis_Acq_${i}.py
echo -e "deeplabcut.create_labeled_video('/projects/b1090/Users/sajiv/DLC-DATA/Explore-Sajiv-2023-08-18/config.yaml',['/projects/b1090/Users/sajiv/DLC-DATA/RatVideos/NOR10_Acq_R${i}.mp4'], videotype='.mp4', draw_skeleton = True)" >> $jobs/Analysis_Acq_${i}.py

echo  "#!/bin/bash
#SBATCH -A p32044
#SBATCH -p gengpu
#SBATCH -t 5:00:00
#SBATCH -N 1
#SBATCH --mem=0
#SBATCH --nodes=1
#SBATCH --output=$jobs/Analysis_Acq_${i}.out" > $jobs/Analysis_Acq_${i}.sh

echo " " >> $jobs/Analysis_Acq_${i}.sh

echo "module load deeplabcut/2.2.0.2" >> $jobs/Analysis_Acq_${i}.sh

echo "python3 $jobs/Analysis_Acq_${i}.py" >> $jobs/Analysis_Acq_${i}.sh

sbatch $jobs/Analysis_Acq_${i}.sh

done

for i in {1..18};
do

echo -e "import deeplabcut" >> $jobs/Analysis_Disc_${i}.py
echo -e "deeplabcut.analyze_videos('/projects/b1090/Users/sajiv/DLC-DATA/Explore-Sajiv-2023-08-18/config.yaml',['/projects/b1090/Users/sajiv/DLC-DATA/RatVideos/NOR10_Disc_R${i}.mp4'], save_as_csv=True, videotype='.mp4')" >> $jobs/Analysis_Disc_${i}.py
echo -e "deeplabcut.create_labeled_video('/projects/b1090/Users/sajiv/DLC-DATA/Explore-Sajiv-2023-08-18/config.yaml',['/projects/b1090/Users/sajiv/DLC-DATA/RatVideos/NOR10_Disc_R${i}.mp4'], videotype='.mp4', draw_skeleton = True)" >> $jobs/Analysis_Disc_${i}.py

echo  "#!/bin/bash
#SBATCH -A p32044
#SBATCH -p gengpu
#SBATCH -t 5:00:00
#SBATCH -N 1
#SBATCH --mem=0
#SBATCH --nodes=1
#SBATCH --output=$jobs/Analysis_Disc_${i}.out" > $jobs/Analysis_Disc_${i}.sh

echo " " >> $jobs/Analysis_Disc_${i}.sh

echo "module load deeplabcut/2.2.0.2" >> $jobs/Analysis_Disc_${i}.sh

echo "python3 $jobs/Analysis_Disc_${i}.py" >> $jobs/Analysis_Disc_${i}.sh

sbatch $jobs/Analysis_Disc_${i}.sh


done
``
