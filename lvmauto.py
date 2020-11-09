import subprocess as sp

print("\t\t\tWelcome to the Linux LVM automation Script")
print("\t\t\t------------------------------------------")

while(1):
	print("""
1.Press 1 to get the list of all the disks attached to the system
2.Press 2 to create Physical Volume
3.Press 3 to create Volume Group
4.Press 4 to create Logical Volume
5.Press 5 to increase or decrease the Logical Volume
6.Press 6 to remove the Logical Volume
7.Press 7 to remove the Volume Group
8.Press 8 to remove the Physical Volume
9.Press 9 to format the partition
10.Press 10 to mount the partition
11.Press 11 to get a list of mount targets
12.Press 12 to unmount the partition
13.Press 13 to exit the program\n""")


	choice=int(input("Enter your Choice: "))

	if choice == 1:
		print(sp.getoutput("sudo fdisk -l"))
		input()

	if choice == 2:
		disknameadd = input("\nEnter the disk name: ")
		print(sp.getoutput("sudo pvcreate {}".format(disknameadd)))
		input()

	if choice == 3:
		vgnameadd = input("\nEnter the Volume Group name that you want to keep: ")
		diskNameForVG = input("Enter the disk name(s): ")
		print(sp.getoutput("sudo vgcreate {} {}".format(vgnameadd,diskNameForVG)))
		input()

	if choice == 4:
		lvnameadd = input("\nEnter the Logical Volume name you want: ")
		sizeadd = input("\nEnter the size of the Logical Volume: ")
		vgNameForLV = input("\nEnter the name of the Volume Group from where you want to take your storage space: ")
		print(sp.getoutput("sudo lvcreate --size {} --name {}  {} -y ".format(sizeadd,lvnameadd,vgNameForLV)))
		input()

	if choice == 5:
		sizeExtend = input("\nEnter the Size to extend the Partition (K,M,G,T,P): ")
		partitionExtend = input("\nEnter the Logical Partition in the format /dev/<Volume Group Name>/<Logical Volume Name>: ")
		print(sp.getoutput("sudo lvextend --size +{} {}".format(sizeExtend,partitionExtend)))
		print(sp.getoutput("sudo resize2fs {}".format(partitionExtend)))
		input()

	if choice == 6:
		lvnamerm = input("\nEnter the Logical Volume name you want to remove: ")
		vgNameForRM = input("\nEnter the Volume Group name associated with the Logical Volume: ")
		print(sp.getoutput("sudo lvremove /dev/{}/{} -y ".format(vgNameForRM,lvnamerm)))
		input()

	if choice == 7:
		vgnamerm = input("\nEnter the Volume Group name that you want to remove: ")
		print(sp.getoutput("sudo vgremove {}".format(vgnamerm)))
		input()
	
	if choice == 8:
		disknamerm = input("\nEnter the disk name: ")
		print(sp.getoutput("sudo pvremove {}".format(disknamerm)))
		input()
		
	if choice == 9:
		formatPartition = input("\nEnter the Logical Partition in the format /dev/<Volume Group Name>/<Logical Volume Name>: ")
		print(sp.getoutput("sudo mkfs.ext4 {}".format(formatPartition)))
		input()

	if choice == 10:
		mountTarget = input("\nEnter the mount target: ")
		mountPartition = input("\nEnter the Partition in the format /dev/<Volume Group Name>/<Logical Volume Name>: ")
		print(sp.getoutput("sudo mount {} {}".format(mountPartition,mountTarget)))
		input()

	if choice == 11:
		print(sp.getoutput("sudo df -h"))
		input()

	if choice == 12:
		unmountPartition = input("\nEnter the Partition in the format /dev/<Volume Group Name>/<Logical Volume Name>: ")
		print(sp.getoutput("sudo umount {}".format(unmountPartition)))
		input()

	if choice == 13:
		exit()
	print(sp.getoutput("clear"))

