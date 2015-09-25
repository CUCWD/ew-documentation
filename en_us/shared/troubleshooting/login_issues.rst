.. Typical login issues will be descriped here.

.. include:: ../../../shared/links.rst

.. _Login Issues:

##############################
Login Issues
##############################

Here are some typical issues that a user could be dealing with when trying to login
to EducateWorkforce.

.. contents::
 :local:
 :depth: 1

All accounts on EducateWorkforce utilize the first-party login method.  With *Connected Account* functionality on the
:ref:`Account Settings<SFD Account Settings>` page, additional third-party accounts can be linked to existing
first-party accounts.  Please use the :ref:`Provider Login Denied<SFD Provider Login Denied>` section to diagnose and
repair this linking.

.. list-table::
  :widths: 10 60
  :header-rows: 1

  * - Login Method
    - Description
  * - ``first-party``
    - The default login requests two fields *Email* and *Password* to authenticate.  Validating authentication credentials is
      handled by EducateWorkforce.
  * - ``third-party``
    - Refers to the provider login for additional services (e.g. Facebook, LinkedIn, Google, University/Institution).
      Validating authentication credentials is handled by the provider.

.. _SFD Login Invalid:

***************************************************************
Login Invalid
***************************************************************

Invalid first-party *Email* or *Password* fields will product this error message.  Enter in the correct login
credentials to gain access to the :ref:`Dashboard<SFD Learner Dashboard>` page.  Should that not work please follow the
:ref:`Password Reset<SFD Password Reset>` instructions before contacting `support@educateworkforce.com`_.

.. image:: ../../../shared/troubleshooting/Images/SFD_Login_Invalid.png
    :width: 700
    :alt: Message displayed when a user tries to login with invalid first-party credentials.

This error is displayed when a valid email exists but more than three login attempts with invalid password have been
processed.

.. note::
   The account lock duration is currently set to fifteen minutes.  If you cannot wait until that period expires, please
   contact `support@educateworkforce.com`_.

.. image:: ../../../shared/troubleshooting/Images/SFD_Login_Invalid_Account_Locked.png
    :width: 700
    :alt: Message displayed when a user tries to login with valid email but invalid password more than three attempts.

.. _SFD Password Reset:

***************************************************************
Password Reset
***************************************************************

If you are having trouble logging in with your EducateWorkforce first-party account please first try resetting your
password from the **Login** page.

This image shows the *Password Assistance* page where the user can reset their password.

.. note::
   The error message indicates that the user entered in an email that doesn't exist in the EducateWorkforce system.
   To resolve this the user would enter in the email that was used during the registration process.  Make sure that you
   have clicked the :ref:`Activation<SFD Activation>` email since this will also produce this error message.

   If you still cannot perform the password reset process, then contact `support@educateworkforce.com`_ to resolve this
   discrepancy with your account.

.. image:: ../../../shared/troubleshooting/Images/SFD_Password_Reset_Email_Invalid.png
    :width: 700
    :alt: Message displayed when a user tries to reset account's password but put an invalid email.

Here is a sample password reset email message.

.. image:: ../../../shared/troubleshooting/Images/SFD_Password_Reset_Email.png
    :width: 700
    :alt: Message displayed when a user resets their EducateWorkforce password.

.. _SFD Provider Login Denied:

***************************************************************
Provider Login Denied
***************************************************************

Every new user for EducateWorkforce creates a first-party account.  These
accounts have the ability to link to an existing third-party provider account.  The warning below indicates
that your first-party account is not correctly setup (linked) to your existing third-party
account.

.. image:: ../../../shared/troubleshooting/Images/SFD_Provider_Login_Denied.png
    :width: 700
    :alt: Message displayed when a user logs into a third-party provider but doesn't have this provider linked to their
          EducateWorkforce first-party account.

You can go to your :ref:`Account Settings<SFD Account Settings>` page to re-link your first-party EducateWorkforce account
to an existing third-party account by following these steps.

#. Click the *Reset Password* link from the **Login** page.  Enter the email account that was used when creating your
   EducateWorkforce first-party account during registration.  After submitting the password reset request an email
   will be generated.  Click the provided link in the email and enter in new password credentials.
#. Proceed to the **Login** page and enter your new authentication credentials.
#. From the :ref:`Dashboard<SFD Learner Dashboard>` page select the arrow next to your username, in the upper right
   corner, to view the :ref:`Account Settings<SFD Account Settings>` page.  The *Connected Accounts* section
   provides the user with linking first-party EducateWorkforce accounts to existing third-party provider accounts.
   Please click the *Link* button next to the provider to connect the accounts and the *Unlink* button to disconnect them.

   .. note::
      The third-party provider may require you to login upon linking of these accounts. Issues with this login will need
      to be addressed by the third-party provider, not EducateWorkforce support.

#. Log out after successful linking of first-party EducateWorkforce and third-party provider accounts.
#. Proceed to the **Login** page, then click the *Provider Log In* button which will display a list of
   available third-party providers.

   .. note::
      Please let `support@educateworkforce.com`_ know if your third-party provider is missing from the available list.

#. Select your third-party provider and authenticate with their login page.  After successful login you will be
   redirected to the :ref:`Dashboard<SFD Learner Dashboard>` page.  Single Sign-On (SSO) with your third-party should be
   working now for EducateWorkforce.


