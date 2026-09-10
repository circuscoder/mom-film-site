/* The only provider integration point. Public settings only; never put API secrets here.
   Contract and activation checklist: README.md. */
window.MOM_SIGNUP = Object.freeze({
  endpoint: '',
  emailField: 'email',
  extraFields: {},
  // Return true only when the provider confirms it accepted the subscription.
  isAccepted: function (response, body) {
    return response.ok && body && body.success === true;
  },
  successMessage: 'Your request was received. Check your inbox for the next step.'
});
