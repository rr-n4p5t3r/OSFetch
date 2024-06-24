import platform
import distro
from colorama import Fore, Style

class SystemLogo:
    @staticmethod
    def get_os_logo():
        """
        Obtiene el logo ASCII del sistema operativo y lo colorea según la distribución de Linux.
        """
        os_name = platform.system()

        if os_name == "Linux":
            dist_info = distro.linux_distribution()
            dist_name = dist_info[0].lower()
            if "debian" in dist_name:
                return f"{Fore.RED}" + """
                    _,met$$$$$gg.
                    ,g$$$$$$$$$$$$$$$P.
                ,g$$P'            'Y$$.".
                ,$$P'              `$$$.
                ',$$P       ,ggs.     `$$b:
                `d$$'     ,$P\"   .    $$$
                $$P      d$'     ,    $$P
                $$:      $$.   -    ,d$$'
                $$;      Y$b._   _,d$P'
                Y$$.    `. `"Y$$$$P"'
                `$$b      "-.__
                `Y$$
                    `Y$$.
                    `$$b.
                        `Y$$b.
                            `"Y$b._
                """
            
            elif "ubuntu" in dist_name:
                return f"{Fore.YELLOW}" + """
                        ./oydmMMMMMMmdyo/.
                        :smMMMMMMMMMMMhs+:++yhs:
                    `omMMMMMMMMMMMN+`        `odo`
                    /NMMMMMMMMMMMMN-            `sN/
                `hMMMMmhhmMMMMMMh               sMh`
                .mMmo-     /yMMMMm`              `MMm.
                mN/       yMMMMMMMd-              MMMm
                oN-        oMMMMMMMMMms+//+o+:    :MMMMo
                m/          +NMMMMMMMMMMMMMMMMm. :NMMMMm
                M`           .NMMMMMMMMMMMMMMMNodMMMMMMM
                M-            sMMMMMMMMMMMMMMMMMMMMMMMMM
                mm`           mMMMMMMMMMNdhhdNMMMMMMMMMm
                oMm/        .dMMMMMMMMh:      :dMMMMMMMo
                mMMNyo/:/sdMMMMMMMMM+          sMMMMMm
                .mMMMMMMMMMMMMMMMMMs           `NMMMm.
                `hMMMMMMMMMMM.oo+.            `MMMh`
                    /NMMMMMMMMMo                sMN/
                    `omMMMMMMMMy.            :dmo`
                        :smMMMMMMMh+-`   `.:ohs:
                        ./oydmMMMMMMdhyo/.
                """

            elif "mint" in dist_name:
                return f"{Fore.GREEN}" + """
                            ...-:::::-...
                        .-MMMMMMMMMMMMMMM-.
                    .-MMMM`..-:::::::-..`MMMM-.
                    .:MMMM.:MMMMMMMMMMMMMMM:.MMMM:.
                -MMM-M---MMMMMMMMMMMMMMMMMMM.MMM-
                `:MMM:MM`  :MMMM:....::-...-MMMM:MMM:`
                :MMM:MMM`  :MM:`  ``    ``  `:MMM:MMM:
                .MMM.MMMM`  :MM.  -MM.  .MM-  `MMMM.MMM.
                :MMM:MMMM`  :MM.  -MM-  .MM:  `MMMM-MMM:
                :MMM:MMMM`  :MM.  -MM-  .MM:  `MMMM:MMM:
                :MMM:MMMM`  :MM.  -MM-  .MM:  `MMMM-MMM:
                .MMM.MMMM`  :MM:--:MM:--:MM:  `MMMM.MMM.
                :MMM:MMM-  `-MMMMMMMMMMMM-`  -MMM-MMM:
                :MMM:MMM:`                `:MMM:MMM:
                .MMM.MMMM:--------------:MMMM.MMM.
                    '-MMMM.-MMMMMMMMMMMMMMM-.MMMM-'
                    '.-MMMM``--:::::--``MMMM-.'
                            '-MMMMMMMMMMMMM-'
                            ``-:::::-``
                """

            elif "fedora" in dist_name:
                return f"{Fore.BLUE}" + """
                            .',;::::;,'.
                        .';:cccccccccccc:;,.
                    .;cccccccccccccccccccccc;.
                    .:cccccccccccccccccccccccccc:.
                .;ccccccccccccc;.dddl:.;ccccccc;.
                .:ccccccccccccc;OWMKOOXMWd;ccccccc:.
                .:ccccccccccccc;KMMc;cc;xMMc;ccccccc:.
                ,cccccccccccccc;MMM.;cc.;WW:;cccccccc,
                :cccccccccccccc;MMM.;cccccccccccccccc:
                :ccccccc;oxOOOo;MMM0OOk.;cccccccccccc:
                cccccc;0MMKxdd:;MMMkddc.;cccccccccccc;
                ccccc;XM0';cccc;MMM.;cccccccccccccccc'
                ccccc;MMo;ccccc;MMW.;ccccccccccccccc;
                ccccc;0MNc.;ccc.xMMd;ccccccccccccccc;
                cccccc;dNMWXXXWM0:;cccccccccccccc:;
                cccccccc.;odl:.;cccccccccccccc:,.
                :cccccccccccccccccccccccccccc:'.
                .:cccccccccccccccccccccc:;,..
                '::cccccccccccccc::;,.
                """

            else:
                return "Unsupported Linux Distribution"
        
        elif os_name == "Windows 11" or os_name == "Windows 10" or os_name == "Windows 8" or os_name == "Windows":
            return f"{Fore.CYAN}" + """
            ################  ################
            ################  ################
            ################  ################
            ################  ################
            ################  ################
            ################  ################
            ################  ################

            ################  ################
            ################  ################
            ################  ################
            ################  ################
            ################  ################
            ################  ################
            ################  ################
            """
        
        elif os_name == "Mac OS X" or os_name == "macOS" or os_name == "OS X":
            return f"{Fore.WHITE}" + """
                                c.'
                            ,xNMM.
                        .OMMMMo
                        lMMM"
                .;loddo:.  .olloddol;.
            cKMMMMMMMMMMNWMMMMMMMMMM0:
            .KMMMMMMMMMMMMMMMMMMMMMMMWd.
            XMMMMMMMMMMMMMMMMMMMMMMMX.
            ;MMMMMMMMMMMMMMMMMMMMMMMM:
            :MMMMMMMMMMMMMMMMMMMMMMMM:
            .MMMMMMMMMMMMMMMMMMMMMMMMX.
            kMMMMMMMMMMMMMMMMMMMMMMMMWd.
            'XMMMMMMMMMMMMMMMMMMMMMMMMMMk
            'XMMMMMMMMMMMMMMMMMMMMMMMMK.
              kMMMMMMMMMMMMMMMMMMMMMMd
               ;KMMMMMMMWXXWMMMMMMMk.
                "cooc*"    "*coo'"
            """            
        
        else:
            return "Unsupported OS"
