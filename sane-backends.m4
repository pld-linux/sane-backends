# from acinclude.m4 for sane-frontends
# ********************************************************************
# Configure paths for SANE 
# Oliver Rauch 2000-10-30

dnl AM_PATH_SANE([MINIMUM-VERSION, [ACTION-IF-FOUND [, ACTION-IF-NOT-FOUND]]])
dnl Test for SANE, and define SANE_CFLAGS and SANE_LIBS
dnl
AC_DEFUN(AM_PATH_SANE,
[dnl 
dnl Get the cflags and libraries from the sane-config script
dnl
AC_ARG_WITH(sane-prefix,[  --with-sane-prefix=PFX  Prefix where SANE is installed (optional)],
            sane_config_prefix="$withval", sane_config_prefix="")
AC_ARG_WITH(sane-exec-prefix,[  --with-sane-exec-prefix=PFX Exec prefix where SANE is installed (optional)],
            sane_config_exec_prefix="$withval", sane_config_exec_prefix="")
AC_ARG_ENABLE(sanetest, [  --disable-sanetest      Do not try to compile and run a test SANE program], , enable_sanetest=yes)

  if test x$sane_config_exec_prefix != x ; then
     sane_config_args="$sane_config_args --exec-prefix=$sane_config_exec_prefix"
     if test x${SANE_CONFIG+set} != xset ; then
        SANE_CONFIG=$sane_config_exec_prefix/bin/sane-config
     fi
  fi
  if test x$sane_config_prefix != x ; then
     sane_config_args="$sane_config_args --prefix=$sane_config_prefix"
     if test x${SANE_CONFIG+set} != xset ; then
        SANE_CONFIG=$sane_config_prefix/bin/sane-config
     fi
  fi

  AC_PATH_PROG(SANE_CONFIG, sane-config, no)
  min_sane_version=ifelse([$1], ,1.0.0,$1)
  AC_MSG_CHECKING(for SANE - version >= $min_sane_version)
  no_sane=""
  if test "$SANE_CONFIG" = "no" ; then
    no_sane=yes
  else
    SANE_CFLAGS=`$SANE_CONFIG $sane_config_args --cflags`
    SANE_LDFLAGS=`$SANE_CONFIG $sane_config_args --ldflags`
#    SANE_LIBS=`$SANE_CONFIG $sane_config_args --libs`
    SANE_LIBS=`$SANE_CONFIG $sane_config_args --libs | sed -e 's/-lintl//g'`
    SANE_PREFIX=`$SANE_CONFIG $sane_config_args --prefix`
    sane_config_major_version=`$SANE_CONFIG $sane_config_args --version | \
           sed 's/\([[0-9]]*\).\([[0-9]]*\).\([[0-9]]*\)/\1/'`
    sane_config_minor_version=`$SANE_CONFIG $sane_config_args --version | \
           sed 's/\([[0-9]]*\).\([[0-9]]*\).\([[0-9]]*\)/\2/'`
    sane_config_micro_version=`$SANE_CONFIG $sane_config_args --version | \
           sed 's/\([[0-9]]*\).\([[0-9]]*\).\([[0-9]]*\)/\3/'`
    if test "x$enable_sanetest" = "xyes" ; then
      ac_save_CFLAGS="$CFLAGS"
      ac_save_LDFLAGS="$LDFLAGS"
      ac_save_LIBS="$LIBS"
      CFLAGS="$CFLAGS $SANE_CFLAGS"
      LDFLAGS="$LDFLAGS $SANE_LDFLAGS"
      LIBS="$LIBS $SANE_LIBS"
dnl
dnl Now check if the installed SANE is sufficiently new. (Also sanity
dnl checks the results of sane-config to some extent
dnl
      rm -f conf.sanetest
      AC_TRY_RUN([
#include <sane/sane.h>
#include <stdio.h>

int 
main ()
{
  int major, minor, micro;

  system ("touch conf.sanetest");

  if (sscanf("$min_sane_version", "%d.%d.%d", &major, &minor, &micro) != 3) {
     printf("%s, bad version string\n", "$min_sane_version");
     exit(1);
   }

   if ( ($sane_config_major_version == major) &&
        ( ($sane_config_minor_version > minor) ||
          ( ($sane_config_minor_version == minor) && ($sane_config_micro_version >= micro))))
   {
     return 0;
   }
   else if ($sane_config_major_version > major)
   {
     printf("\n*** A too new version of SANE (%d.%d.%d) was found.\n",
            $sane_config_major_version, $sane_config_minor_version, $sane_config_micro_version);
     printf("*** You need a version of SANE with the major version number %d.\n", major);
   }
   else
   {
     printf("\n*** An old version of SANE (%d.%d.%d) was found.\n",
            $sane_config_major_version, $sane_config_minor_version, $sane_config_micro_version);
     printf("*** You need a version of SANE newer than %d.%d.%d. The latest version of\n",
            major, minor, micro);
   }

   printf("*** SANE is always available from ftp://ftp.mostang.com\n");
   printf("***\n");
   printf("*** If you have already installed a sufficient version, this error\n");
   printf("*** probably means that the wrong copy of the sane-config shell script is\n");
   printf("*** being found. The easiest way to fix this is to remove the old version\n");
   printf("*** of SANE, but you can also set the SANE_CONFIG environment to point to the\n");
   printf("*** correct copy of sane-config. (In this case, you will have to\n");
   printf("*** modify your LD_LIBRARY_PATH enviroment variable, or edit /etc/ld.so.conf\n");
   printf("*** so that the correct libraries are found at run-time))\n");

  return 1;
}
],, no_sane=yes,[echo $ac_n "cross compiling; assumed OK... $ac_c"])
       CFLAGS="$ac_save_CFLAGS"
       LDFLAGS="$ac_save_LDFLAGS"
       LIBS="$ac_save_LIBS"
     fi
  fi
  if test "x$no_sane" = x ; then
     AC_MSG_RESULT(yes)
     ifelse([$2], , :, [$2])     
  else
     AC_MSG_RESULT(no)
     if test "$SANE_CONFIG" = "no" ; then
       echo "*** The sane-config script installed by SANE could not be found"
       echo "*** If SANE was installed in PREFIX, make sure PREFIX/bin is in"
       echo "*** your path, or set the SANE_CONFIG environment variable to the"
       echo "*** full path to sane-config."
     else
       if test -f conf.sanetest ; then
        :
       else
          echo "*** Could not run SANE test program, checking why..."
          CFLAGS="$CFLAGS $SANE_CFLAGS"
          LIBS="$LIBS $SANE_LIBS"
          LDFLAGS="$LDFLAGS $SANE_LDFLAGS"
          AC_TRY_LINK([
#include <sane/sane.h>
#include <stdio.h>
],      [ return (SANE_CURRENT_MAJOR); ],
        [ echo "*** The test program compiled, but did not run. This usually means"
          echo "*** that the run-time linker is not finding SANE or finding the wrong"
          echo "*** version of SANE. If it is not finding SANE, you'll need to set your"
          echo "*** LD_LIBRARY_PATH environment variable, or edit /etc/ld.so.conf to point"
          echo "*** to the installed location.  Also, make sure you have run ldconfig if that"
          echo "*** is required on your system."
	  echo "***"
          echo "*** If you have an old version installed, it is best to remove it, although"
          echo "*** you may also be able to get things to work by modifying LD_LIBRARY_PATH"
          echo "***" ],
        [ echo "*** The test program failed to compile or link. See the file config.log for the"
          echo "*** exact error that occured. This usually means SANE was incorrectly installed"
          echo "*** or that you have moved SANE since it was installed. In the latter case, you"
          echo "*** may want to edit the sane-config script: $SANE_CONFIG" ])
          CFLAGS="$ac_save_CFLAGS"
          LDFLAGS="$ac_save_LDFLAGS"
          LIBS="$ac_save_LIBS"
       fi
     fi
     SANE_CFLAGS=""
     SANE_LDFLAGS=""
     SANE_LIBS=""
     ifelse([$3], , :, [$3])
  fi
  AC_SUBST(SANE_LDFLAGS)
  AC_SUBST(SANE_CFLAGS)
  AC_SUBST(SANE_LIBS)
  AC_SUBST(SANE_PREFIX)
  rm -f conf.sanetest
])
