function authorize(allowedRoles) {
  return (req, res, next) => {
    const role = req && req.user ? req.user.role : undefined;
    if (allowedRoles.includes(role)) {
      next();
    } else {
      res.status(403).send('Forbidden');
    }
  };
}

module.exports = authorize;
