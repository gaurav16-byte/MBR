# MBR (Master Boot Record)

## Partition Types
| Hex Code | Description                                                                                                                                                 |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 00       | Should NOT be used in an actual table entry! It does not indicate an unknown type, but rather an empty entry; in which case, all other fields should be zero |
| 01       | 12-bit FAT (on hard disks, not floppy disks, so you'll rarely see this today).                                                                              |
| 02       | XENIX root                                                                                                                                                  |
| 03       | XENIX /usr (obsolete)                                                                                                                                       |
| 04       | 16-bit FAT, partition; of sizes less than 32 MB.                                                                                                            |
| 05       | Extended Partition; within the first 1024 cylinders of a disk drive.                                                                                        |
| 06       | 16-bit FAT, partition; greater than or equal to 32 MB.                                                                                                      |
| 07       | Installable file systems: HPFS or NTFS. Also, QNX and Advanced Unix.                                                                                        |
| 08       | AIX bootable partition, AIX (Linux), SplitDrive, OS/2 (v1.3), Dell partition spanning multiple drives, Commodore DOS.                                       |
| 09       | AIX data partition, AIX bootable (Linux), Coherent file system, QNX.                                                                                        |
| 0A       | Coherent swap partition, OPUS or OS/2 Boot Manager.                                                                                                         |
| 0B       | 32-bit FAT                                                                                                                                                  |
| 0C       | 32-bit FAT, using INT 13 Extensions.                                                                                                                        |
| 0E       | 16-bit FAT >= 32 MB, using INT 13 Extensions.                                                                                                               |
| 0F       | Extended Partition, using INT 13 Extensions; often begins past cylinder 1024.                                                                               |
| 10       | OPUS                                                                                                                                                        |
| 11       | Hidden 12-bit FAT.                                                                                                                                          |
| 12       | Compaq diagnostics.                                                                                                                                        |
| 14       | Hidden 16-bit FAT, partition <32 MB, Novell DOS 7.0, AST DOS with logical sectored FAT.                                                                     |
| 16       | Hidden 16-bit FAT, partition >= 32 MB                                                                                                                       |
| 17       | Hidden IFS (HPFS, NTFS).                                                                                                                                    |
| 18       | AST Windows swap file                                                                                                                                       |
| 19       | Willowtech Photon coS                                                                                                                                       |
| 1B       | Hidden 32-bit FAT                                                                                                                                           |
| 1C       | Hidden 32-bit FAT, Ext INT 13                                                                                                                               |
| 1E       | Hidden 16-bit FAT >32 MB, Ext. INT 13 (PowerQuest specific)                                                                                                |
| 20       | Willowsoft Overture File System (OFS1)                                                                                                                      |
| 21       | Reserved (HP Volume Expansion, SpeedStor variant), Oxygen FSo2                                                                                              |
| 22       | Oxygen Extended                                                                                                                                             |
| 23       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 24       | NEC MS-DOS 3.x                                                                                                                                              |
| 26       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 31       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 33       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 34       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 36       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 38       | Theos                                                                                                                                                       |
| 3C       | PowerQuest Files Partition Format                                                                                                                           |
| 3D       | Hidden NetWare                                                                                                                                              |
| 40       | VENIX 80286                                                                                                                                                 |
| 41       | Personal RISC Boot, PowerPC boot partition, PTS-DOS 6.70, Minix and DR-DOS.                                                                                 |
| 42       | Secure File System, Windows 2000/XP (NT 5): Dynamic extended partition, PTS-DOS 6.70, DR-DOS swap.                                                          |
| 43       | Alternative Linux native file system (EXT2fs), PTS-DOS 6.70, DR-DOS                                                                                         |
| 45       | Priam, EUMEL/Elan                                                                                                                                           |
| 46       | EUMEL/Elan                                                                                                                                                  |
| 47       | EUMEL/Elan                                                                                                                                                  |
| 48       | EUMEL/Elan                                                                                                                                                  |
| 4A       | ALFS/THIN lightweight filesystem for DOS                                                                                                                    |
| 4D       | QNX                                                                                                                                                         |
| 4E       | QNX                                                                                                                                                         |
| 4F       | QNX, Oberon boot/data partition                                                                                                                             |
| 50       | Ontrack Disk Manager, read-only partition, FAT partition                                                                                                    |
| 51       | Ontrack Disk Manager, read/write partition, FAT partition                                                                                                   |
| 52       | CP/M, Microport System V/386                                                                                                                                |
| 53       | Ontrack Disk Manager, write-only                                                                                                                            |
| 54       | Ontrack Disk Manager 6.0 (DDO)                                                                                                                              |
| 55       | EZ-Drive 3.05                                                                                                                                               |
| 56       | Golden Bow VFeature                                                                                                                                        |
| 5C       | Priam EDISK                                                                                                                                                 |
| 61       | Storage Dimensions SpeedStor                                                                                                                                |
| 63       | GNU HURD, Mach, MtXinu BSD 4.2 on Mach, Unix Sys V/386, 386/ix                                                                                              |
| 64       | Novell NetWare 286, SpeedStore                                                                                                                              |
| 65       | Novell NetWare (3.11 and 4.1)                                                                                                                               |
| 66       | Novell NetWare 386                                                                                                                                          |
| 67       | Novell NetWare                                                                                                                                              |
| 68       | Novell NetWare                                                                                                                                              |
| 69       | Novell NetWare 5+, Novell Storage Services (NSS)                                                                                                            |
| 70       | DiskSecure Multi-Boot                                                                                                                                       |
| 75       | IBM PC/IX                                                                                                                                                   |
| 80       | Minix v1.1 - 1.4a, Old MINIX (Linux)                                                                                                                        |
| 81       | Linux/Minix v1.4b+, Mitac Advanced Disk Manager                                                                                                             |
| 82       | Linux Swap partition, Prime or Solaris (Unix)                                                                                                               |
| 83       | Linux native file systems (ext2/3/4, JFS, Reiser, xiafs, and others)                                                                                        |
| 84       | OS/2 hiding type 04h partition, APM hibernation, used by Win98.                                                                                             |
| 86       | NT Stripe Set, Volume Set?                                                                                                                                  |
| 87       | NT Stripe Set, Volume Set?, HPFS FT mirrored partition                                                                                                      |
| 93       | Amoeba file system, Hidden Linux EXT2 partition (PowerQuest)                                                                                                |
| 94       | Amoeba bad block table                                                                                                                                      |
| 99       | Mylex EISA SCSI                                                                                                                                             |
| 9F       | BSDI                                                                                                                                                        |
| A0       | Phoenix NoteBios Power Management "Save to Disk", IBM hibernation                                                                                           |
| A1       | HP Volume Expansion (SpeedStor variant)                                                                                                                     |
| A5       | FreeBSD/386                                                                                                                                                 |
| A6       | OpenBSD, HP Volume Expansion (SpeedStor variant)                                                                                                            |
| A7       | NextStep Partition                                                                                                                                          |
| A9       | NetBSD                                                                                                                                                      |
| AA       | Olivetti DOS with FAT12                                                                                                                                     |
| B0       | Bootmanager BootStar by Star-Tools GmbH                                                                                                                     |
| B7       | BSDI file system or secondarily swap                                                                                                                        |
| B8       | BSDI swap partition or secondarily file system                                                                                                              |
| BE       | Solaris boot partition                                                                                                                                      |
| C0       | Novell DOS/OpenDOS/DR-OpenDOS/DR-DOS secured partition                                                                                                      |
| C1       | DR-DOS 6.0 LOGIN.EXE-secured 12-bit FAT partition                                                                                                           |
| C4       | DR-DOS 6.0 LOGIN.EXE-secured 16-bit FAT partition                                                                                                           |
| C6       | DR-DOS 6.0 LOGIN.EXE-secured Huge partition, or corrupted FAT16 volume/stripe set (Windows NT)                                                              |
| C7       | Syrinx, Cyrnix, HPFS FT disabled mirrored partition, or corrupted NTFS volume/stripe set                                                                    |
| CB       | DR-DOS secured FAT32                                                                                                                                       |
| CE       | DR-DOS secured FAT16X (LBA)                                                                                                                                 |
| D0       | Multiuser DOS secured (FAT12?)                                                                                                                              |
| D1       | Old Multiuser DOS secured FAT12                                                                                                                             |
| D4       | Old Multiuser DOS secured FAT16 (<= 32M)                                                                                                                    |
| DF       | BootIt EMBRM                                                                                                                                               |
| E1       | SpeedStor 12-bit FAT Extended partition, DOS access                                                                                                        |
| E4       | SpeedStor 16-bit FAT Extended partition                                                                                                                     |
| EB       | BeOS file system                                                                                                                                           |
| EE       | Indicates a GPT Protective MBR followed by a GPT/EFI Header.                                                                                                |
| EF       | EFI/UEFI System Partition (or ESP); defines a UEFI system partition                                                                                         |
| F2       | DOS 3.3+ secondary partition                                                                                                                                |
| F4       | SpeedStor                                                                                                                                                |
| F7       | Partitions which span multiple drives, Advanced UNIX                                                                                                                                     |
| FB       | VMware file system partition                                                                                                                                                                                                                                                                                              |
| FC       | VMware swap partition                                                                                                                                       |
| FD       | Linux raid partition                                                                                                                                              |
| FE       | LANstep                                                                                                                                                                                                                       |
| FF       | BBt assistant partition, Older XENIX or Novel Netware                                                                                                                                                 |
